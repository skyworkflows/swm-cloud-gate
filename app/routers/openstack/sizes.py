import typing

from fastapi import APIRouter, Header

from .connector import OpenStackConnector
from .models import ImageInfo, convert_to_flavor

CONNECTOR = OpenStackConnector()
EMPTY_HEADER = Header(None)
ROUTER = APIRouter()


@ROUTER.get("/openstack/flavors")
async def list_flavors(username: str = EMPTY_HEADER, password: str = EMPTY_HEADER):
    CONNECTOR.reinitialize(username, password, "compute")
    flavor_list: typing.List[ImageInfo] = []
    if sizes := CONNECTOR.list_sizes():
        for item in sizes:
            flavor_list.append(convert_to_flavor(item))
    return {"flavors": flavor_list}
