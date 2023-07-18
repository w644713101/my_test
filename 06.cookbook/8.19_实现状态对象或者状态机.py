class ConnectionState:
    """状态的基类"""
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


class ClosedConnectionState(ConnectionState):
    """如果是关闭状态，就要打开，覆写open方法"""
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already close')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('into OpenConnectionState read func')

    @staticmethod
    def write(conn, data):
        print('into OpenConnectionState write func')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.new_state(ConnectionState)


class Connection:
    """每个状态对应一个类，避免大量的if判断"""
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)



