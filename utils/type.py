from enum import Enum


class Type(Enum):
    CHARACTER = "Character"
    LOCATION = "Location"
    ITEM = "Item"
    PICKUPABLE = "Pickupable"
    ROUTE = "Route"
    ROUTE_BLOCK = "RouteBlock"
