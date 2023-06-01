def singleton(_cls):
    """
    Simple realization singleton pattern based on function decoration
    and dictionary cache
    :param _cls: Any class that will be decorated
    :return: Instance of class
    """
    _instances = {}

    def _decorator(*args, **kwargs):
        return _instances.setdefault(_cls, _cls(*args, **kwargs))

    return _decorator
