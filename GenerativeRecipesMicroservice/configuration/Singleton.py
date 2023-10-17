# nice SO yielded this, https://stackoverflow.com/a/11517201/9505707
# which really refers to this, https://www.python.org/download/releases/2.2/descrintro/#__new__
class Singleton(object):
    """Use to create a singleton"""
    def __new__(cls, *args, **kwds):
        """
        >>> s = Singleton()
        >>> p = Singleton()
        >>> id(s) == id(p)
        True
        """
        it_id = "__it__"
        # getattr will dip into base classes, so __dict__ must be used
        it = cls.__dict__.get(it_id, None)
        if it is not None:
            return it
        it = object.__new__(cls)
        setattr(cls, it_id, it)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        '''Subclasses of Singleton should override init instead of __init__. This method is called once-per instance.'''
        pass