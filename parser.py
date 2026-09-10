


class parser():
    nb_drones:int = -1
    hubs = []
    conection = []
    cordinates = []
    color = []
    zone = []
    max_drones = []


    def parser(self):
        with open("01_linear_path.txt", 'r') as f:
            for num , line in enumerate(f):
                if "#" in line :
                    line = line.split("#")[0]
                if not line.strip():
                    continue
                lis = line.split()
                if lis[0]== "nb_drones:":
                    # print(lis)
                    try:
                        if int(lis[1]) > 0:
                             self.nb_drones = lis[1]
                    except Exception :
                        raise ValueError("number of drones must be a number positive!")
                    print(self.nb_drones)
                    break
                else:
                    print("error")
                    break
            for num , line in enumerate(f):
                if not line.strip():
                    continue
                lis1 = line.split()
                if lis1[0] == "connection:":
                    cone = lis1[1].split("-")
                    if cone[0] and cone[1] not in self.hubs:
                        print("error connection", num, self.hubs)
                        break
                if lis1[0].strip() =="start_hub:":
                    self.hubs.append(lis1[1])
                    try:
                        tu = (int(lis1[2]), int(lis1[3]))
                        self.cordinates.append(tu)
                    except:
                        print("error corrdinate", line, isinstance(lis1[2], int))
                        break
                    if len(lis1) == 5 :
                        metadata = lis1[4].strip("[]").split()
                        for data in metadata:
                            meta = data.split("=")
                            if meta[0]== "color":
                                self.color.append(meta[1])
                            elif meta[0]== "zone":
                                self.zone.append(meta[1])
                            elif meta == "max_drones":
                                self.max_drones.append(meta[1])
                            else:
                                print("error in metadata line ", line)


                elif lis1[0] == "end_hub:":
                    self.hubs.append(lis1[1])
                    try:
                        tu = (int(lis1[2]), int(lis1[3]))
                        self.cordinates.append(tu)
                    except:
                        print("error corrdinate", line, isinstance(lis1[2], int))
                        break
                    if len(lis1) == 5 :
                        metadata = lis1[4].strip("[]").split()
                        for data in metadata:
                            meta = data.split("=")
                            if meta[0]== "color":
                                self.color.append(meta[1])
                            elif meta[0]== "zone":
                                self.zone.append(meta[1])
                            elif meta == "max_drones":
                                self.max_drones.append(meta[1])
                            else:
                                print("error in metadata line ", line)
                elif lis1[0] == "hub:":
                    if "-" in lis1[1] and " " in lis1:
                        print("hhhhhhhhhhhhhhhhhhh")
                    self.hubs.append(lis1[1])
                    try:
                        tu = (int(lis1[2]), int(lis1[3]))
                        self.cordinates.append(tu)
                    except:
                        print("error corrdinate", line, isinstance(lis1[2], int))
                        break
                    if len(lis1) == 5 :
                        metadata = lis1[4].strip("[]").split()
                        for data in metadata:
                            meta = data.split("=")
                            if meta[0]== "color":
                                self.color.append(meta[1])
                            elif meta[0]== "zone":
                                self.zone.append(meta[1])
                            elif meta == "max_drones":
                                self.max_drones.append(meta[1])
                            else:
                                print("error in metadata line ", line)

                elif lis1[0] == "connection:":
                    con = lis1[1].split("-")
                    if con[0] == con[1]:
                        print("ilegale connection!!!")
                        exit()
                    for h in con:
                        if h not in self.hubs:
                            print("error connection error:::")
                            break
                    if con not in self.conection and con.reverse() not in self.conection:
                        self.conection.append(con)
                    else:
                        print("ERROR")
                        exit()


try:

    pars = parser
    pars.parser(pars)
    print(pars.color)
    print(pars.conection)
    print(pars.cordinates)
    print(pars.hubs)
    print("\n\n\n")
    for i in pars.hubs:
        

except Exception as e:
    print(e)
    