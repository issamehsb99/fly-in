class connection_class:
    def __init__(self):
        self.max_link_capacity: int = 0
        self.neigh = []


class zone_class:
    def __init__(self):
        self.max_drones: int = 1
        self.name: str = ""
        self.zone_type: str = ""
        self.is_start: bool = False
        self.is_end: bool = False
        self.capacity: int = 0
        self.connection = connection_class()


class parser:
    def __init__(self):
        self.nb_drones: int = -1

        self.hubs = []

        self.connection = connection_class().neigh

        self.cordinates = []
        self.color = []
        self.zone = []
        self.max_drones = []

    def parser(self):

        with open("01_linear_path.txt", 'r') as f:

            for num, line in enumerate(f):

                if "#" in line:
                    line = line.split("#")[0]

                if not line.strip():
                    continue

                lis = line.split()

                if lis[0] == "nb_drones:":
                    try:
                        if int(lis[1]) > 0:
                            self.nb_drones = int(lis[1])
                        else:
                            raise ValueError(
                                "number of drones must be positive!"
                            )

                    except Exception:
                        raise ValueError(
                            "number of drones must be a number positive!"
                        )

                    print(self.nb_drones)
                    break

                else:
                    print("error")
                    break

            for num, line in enumerate(f):

                zone = zone_class()

                if "#" in line:
                    line = line.split("#")[0]

                if not line.strip():
                    continue

                lis1 = line.split()

                if lis1[0] == "connection:":
                    cone = lis1[1].split("-")

                    if (
                        not any(h.name == cone[0] for h in self.hubs)
                        or
                        not any(h.name == cone[1] for h in self.hubs)
                    ):
                        print(
                            "error connection",
                            num,
                            self.hubs
                        )
                        break

                if lis1[0].strip() == "start_hub:":

                    zone.name = lis1[1]
                    zone.is_start = True

                    self.hubs.append(zone)

                    try:
                        tu = (
                            int(lis1[2]),
                            int(lis1[3])
                        )

                        self.cordinates.append(tu)

                    except Exception:
                        print(
                            "error corrdinate",
                            line
                        )
                        break

                    if len(lis1) == 5:

                        metadata = lis1[4].strip("[]").split()

                        for data in metadata:

                            meta = data.split("=")

                            if meta[0] == "color":
                                self.color.append(meta[1])

                            elif meta[0] == "zone":
                                self.zone.append(meta[1])
                                zone.zone_type = meta[1]

                            elif meta[0] == "max_drones":
                                self.max_drones.append(meta[1])
                                zone.max_drones = int(meta[1])

                            else:
                                print(
                                    "error in metadata line ",
                                    line
                                )

                elif lis1[0] == "end_hub:":

                    zone.name = lis1[1]
                    zone.is_end = True

                    self.hubs.append(zone)

                    try:
                        tu = (
                            int(lis1[2]),
                            int(lis1[3])
                        )

                        self.cordinates.append(tu)

                    except Exception:
                        print(
                            "error corrdinate",
                            line
                        )
                        break

                    if len(lis1) == 5:

                        metadata = lis1[4].strip("[]").split()

                        for data in metadata:

                            meta = data.split("=")

                            if meta[0] == "color":
                                self.color.append(meta[1])

                            elif meta[0] == "zone":
                                self.zone.append(meta[1])
                                zone.zone_type = meta[1]

                            elif meta[0] == "max_drones":
                                self.max_drones.append(meta[1])
                                zone.max_drones = int(meta[1])

                            else:
                                print(
                                    "error in metadata line ",
                                    line
                                )

                elif lis1[0] == "hub:":

                    zone.name = lis1[1]

                    self.hubs.append(zone)

                    try:
                        tu = (
                            int(lis1[2]),
                            int(lis1[3])
                        )

                        self.cordinates.append(tu)

                    except Exception:
                        print(
                            "error corrdinate",
                            line
                        )
                        break

                    if len(lis1) == 5:

                        metadata = lis1[4].strip("[]").split()

                        for data in metadata:

                            meta = data.split("=")

                            if meta[0] == "color":
                                self.color.append(meta[1])

                            elif meta[0] == "zone":
                                self.zone.append(meta[1])
                                zone.zone_type = meta[1]

                            elif meta[0] == "max_drones":
                                self.max_drones.append(meta[1])
                                zone.max_drones = int(meta[1])

                            else:
                                print(
                                    "error in metadata line ",
                                    line
                                )

                elif lis1[0] == "connection:":

                    con = lis1[1].split("-")

                    if con[0] == con[1]:
                        print("ilegale connection!!!")
                        exit()

                    for h in con:

                        if not any(
                            zone.name == h
                            for zone in self.hubs
                        ):
                            print(
                                "error connection error:::"
                            )
                            break

                    if (
                        con not in self.connection
                        and
                        con[::-1] not in self.connection
                    ):
                        self.connection.append(con)

                    else:
                        print("ERROR")
                        exit()

    def assing_connection(self):

pars = parser()
pars.parser()
print(pars.connection)
for i in pars.hubs:
    print()