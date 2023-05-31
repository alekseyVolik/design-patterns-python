from typing import (
    Iterable,
    Any,
    Optional,
    Tuple,
    Union,
    List
)

import requests
from requests import Response

__REQUEST_PARAMS__ = (
    'url',
    'params',
    'data',
    'json',
    'headers',
    'cookies',
    'files',
    'auth',
    'timeout',
    'allow_redirects',
    'proxies',
    'verify',
    'stream',
    'cert'
)


class DoRequest:
    """
    Класс-делегат. Перенаправляет вызовы методов,
    функциям из модуля request для получения ответа
    (объект requests.Response). Использует параметры
    запроса, переданные при инициализации объекта
    класса
    """

    def __init__(self, **query_params) -> None:
        self.query_params = query_params

    def post(self) -> Response:
        return requests.post(**self.query_params)

    def get(self) -> Response:
        return requests.get(**self.query_params)

    def put(self) -> Response:
        return requests.put(**self.query_params)

    def delete(self) -> Response:
        return requests.delete(**self.query_params)

    def patch(self) -> Response:
        return requests.patch(**self.query_params)


class RequestConfig:

    def __init__(self, **request_params) -> None:
        self.request_params = request_params

    @property
    def do(self) -> DoRequest:
        return DoRequest(**self.request_params)

    def format_url(self,
                   **kwargs
                   ) -> 'RequestConfig':
        url = self.request_params['url'].format(**kwargs)
        self.request_params['url'] = url
        return self

    def set_json(self,
                 json_body: dict
                 ) -> 'RequestConfig':
        self.request_params['json'] = json_body
        return self

    def set_body(self,
                 data: Union[dict, List[Tuple], bytes]
                 ) -> 'RequestConfig':
        self.request_params['data'] = data
        return self

    def set_files(self,
                  files: dict
                  ) -> 'RequestConfig':
        self.request_params['files'] = files
        return self

    def set_get_params(self,
                       payload: dict
                       ) -> 'RequestConfig':
        self.request_params['params'] = payload
        return self


def request_kw_params_validator(name_kw_params: Iterable) -> None:
    unknown_params = [param
                      for param in name_kw_params
                      if param not in __REQUEST_PARAMS__]
    if unknown_params:
        raise ValueError(f'Unknown endpoint parameters: {" ".join(unknown_params)}')


class Endpoint:

    def __init__(self,
                 endpoint: str,
                 from_owner: Optional[tuple] = None,
                 **request_params) -> None:
        request_kw_params_validator(request_params.keys())
        request_kw_params_validator(from_owner)
        self.endpoint = endpoint
        self.from_init = from_owner
        self.request_params = request_params

    def set_url(self, instance: Any) -> None:
        self.request_params['url'] = f'{getattr(instance, "domain", "")}{self.endpoint}'

    def set_params_from_owner(self, instance: Any) -> None:
        for param in self.from_init:
            self.request_params[param] = getattr(instance, param, None)

    def get_request_params(self) -> dict:
        return self.request_params

    def __get__(self, instance, owner):
        self.set_url(instance=instance)
        self.set_params_from_owner(instance=instance)
        return RequestConfig(**self.get_request_params())

    def __set__(self, instance, value):
        raise AttributeError('Cannot change endpoint')
