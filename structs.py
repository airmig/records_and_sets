# choose record types
# immutable with small amount fields use tuple. example coordinates
# to enforce field names use tuple

# small but mutable use a dict
# dict converts to json

# more complicated use a class(needs methods) or dataclass(only data storage)

# for binary use Struct

import concurrent.futures
import logging
from dataclasses import dataclass
from typing import NamedTuple
from struct import Struct
from types import SimpleNamespace
# python 3.7 has dataclasses.dataclass
# better repr method and type checking
@dataclass
class Plane:
    color: str
    engines: int

#python 3.6 has typing.NamedTuple
#the same as namedtuple but allows inheritance
class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

def init():
    return True

def main():
    try:
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(process)d %(levelname)s - %(message)s")
        logging.info("logging configured")
        f16 = Plane("grey", 1)
        logging.info(f16)
        hyundai = Car("white", 24.0, True)
        logging.info(hyundai)
        #tcp/ip header
        # source port 16 bit unsigned short
        # dest port 16 bits
        # sequence 32 bits unsigned long
        # ack # 32 bits

        TCPHeader = Struct("HHLL")
        header = TCPHeader.pack(0x1234, 0x0050, 0x1a, 0x1b)
        logging.info(header)
        rc = TCPHeader.unpack(header)
        logging.info(rc)

        person = SimpleNamespace(first="firstname", last="lastname")
        logging.info(person)

        letters = set(('a','b','c','d','e'))
        letters.add('t')
        ariel = set("ariel")
        logging.info(letters)
        rc = ariel.intersection(letters)
        logging.info(rc)
        let_frozen = frozenset(letters)
        logging.info(let_frozen)

        #multiset a set without unique restrictions known as a bag
        #a counter is set for each element
    except:
        logging.exception("Error in main")
    logging.info("main ended")

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as worker:
        worker.submit(main)
