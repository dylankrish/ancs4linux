from typing import Type, cast
from dasbus.loop import EventLoop  # type: ignore # missing
from dasbus.connection import SystemMessageBus, SessionMessageBus  # type: ignore # missing
from dasbus.server.interface import dbus_interface, dbus_signal  # type: ignore # missing
from dasbus.error import ErrorMapper, DBusError, get_error_decorator  # type: ignore # missing
from dasbus.typing import Bool, Byte, UInt16, Int16, UInt32, Int32  # type: ignore # missing
from dasbus.typing import Str, ObjPath  # type: ignore # missing
from dasbus.typing import Variant  # type: ignore # dynamic

EventLoop = EventLoop
dbus_interface, dbus_signal = dbus_interface, dbus_signal
Bool, Byte, UInt16, Int16, UInt32, Int32 = Bool, Byte, UInt16, Int16, UInt32, Int32
Str, ObjPath = Str, ObjPath
Variant = cast(Type, Variant)

error_mapper = ErrorMapper()
DBusError = DBusError
dbus_error = get_error_decorator(error_mapper)


@dbus_error("org.bluez.Error.Rejected")
class PairingRejected(DBusError):
    pass


def SystemBus() -> SystemMessageBus:
    return SystemMessageBus(error_mapper=error_mapper)


def SessionBus() -> SessionMessageBus:
    return SessionMessageBus(error_mapper=error_mapper)
