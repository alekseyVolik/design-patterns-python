from __future__ import annotations

from typing import Union, List, Tuple
import requests


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

    def post(self) -> requests.Response:
        return requests.post(**self.query_params)

    def get(self) -> requests.Response:
        return requests.get(**self.query_params)

    def put(self) -> requests.Response:
        return requests.put(**self.query_params)

    def delete(self) -> requests.Response:
        return requests.delete(**self.query_params)

    def patch(self) -> requests.Response:
        return requests.patch(**self.query_params)


class RequestBuilder:

    def __init__(self) -> None:
        self.request_params = {}

    def clean(self) -> None:
        self.request_params = {}

    def build(self) -> DoRequest:
        return DoRequest(**self.request_params)

    def set_url(self,
                url: str
                ) -> RequestBuilder:
        self.request_params['url'] = url
        return self

    def set_json(self,
                 json_body: dict
                 ) -> RequestBuilder:
        self.request_params['json'] = json_body
        return self

    def set_body(self,
                 data: Union[dict, List[Tuple], bytes]
                 ) -> RequestBuilder:
        self.request_params['data'] = data
        return self

    def set_files(self,
                  files: dict
                  ) -> RequestBuilder:
        self.request_params['files'] = files
        return self

    def set_get_params(self,
                       payload: dict
                       ) -> RequestBuilder:
        self.request_params['params'] = payload
        return self
