from pywoo.utils.exceptions import WriteOnlyException, ReadOnlyException


class ApiSuperClass(object):
    """
    Main class inherited by all the objects returned by the library.
    """
    _ro_attributes = set()
    """
    A set containing readonly attributes. By default is initialized with attributes from Woocommerce REST API v3.

    *Don't edit this unless you want to use this library with other versions of the Woocommerce REST API.*
    """
    _wo_attributes = set()
    """
    A set containing writeonly attributes. By default is initialized with attributes from Woocommerce REST API v3.

    *Don't edit this unless you want to use this library with other versions of the Woocommerce REST API.*
    """
    _rw_attributes = set()
    """
    A set containing read/write attributes. By default is initialized with attributes from Woocommerce REST API v3.

    *Don't edit this unless you want to use this library with other versions of the Woocommerce REST API.*
    """

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __setattr__(self, key, value):
        """
        :raises ReadOnlyException: if trying to set a readonly attribute
        """
        if key not in self._ro_attributes:
            return super().__setattr__(key, value)
        else:
            raise ReadOnlyException(key)

    def __getattr__(self, item):
        """
        :raises WriteOnlyException: if trying to set a readonly attribute
        """
        if item not in self._wo_attributes:
            return super().__getattr__(item)
        else:
            raise WriteOnlyException(item)


class ApiObject(ApiSuperClass):
    """
    Class used to represent the main object on every response from Woocommerce.

    *Nothing to see here.*
    """
    def __init__(self, api, url, **kwargs):
        super().__init__(**kwargs)
        self._api = api
        self._url = url


class ApiActiveProperty(ApiSuperClass):
    """
    Class used to represent the objects contained in :class:`~pywoo.utils.models.ApiObject` objects.
    Has also additional methods for retrieving data without having to call the main object.

    *Nothing to see here.*
    """
    def __init__(self, api, **kwargs):
        super().__init__(**kwargs)
        self._api = api


class ApiProperty(ApiSuperClass):
    """
    Class used to represent the objects contained in :class:`~pywoo.utils.models.ApiObject` objects.

    *Nothing to see here.*
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MetaData(ApiProperty):
    """
    Class used to represent the meta data about Woocommerce/Wordpress.

    *Nothing to see here.*
    """
    _ro_attributes = {'id'}
    _rw_attributes = {'key', 'value'}
