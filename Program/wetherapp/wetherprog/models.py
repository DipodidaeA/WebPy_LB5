from django.db import models

class DTO:
    Id: int
    Name: str
    D: int
    M: int
    Y: int
    Morn: int
    Noon: int
    Night: int

    def __init__(self, id, name, d, m, y, morn, noon, night):
        self.Id = id
        self.Name = name
        self.D = d
        self.M = m
        self.Y = y
        self.Morn = morn
        self.Noon = noon
        self.Night = night

class Day:
    Id: int
    DateId: int
    TempId: int

    def __init__(self, id: int, dateId: int, tempId: int):
        self.Id = id
        self.DateId = dateId
        self.TempId = tempId

class Date:
    Id: int
    Name: str
    D: int
    M: int
    Y: int

    def __init__(self, id: int, name: str, d: int, m: int, y: int):
        self.Id = id
        self.Name = name
        self.D = d
        self.M = m
        self.Y = y

class Temp:
    Id: int
    Morn: int
    Noon: int
    Night: int

    def __init__(self, id: int, morn: int, noon: int, night: int):
        self.Id = id
        self.Morn = morn
        self.Noon = noon
        self.Night = night

class BaseEntit:
    CountId: int

    def __init__(self):
        self.CountId = 0

    def countUp(self):
        self.CountId += 1
        return self.CountId
    
    def countReset(self):
        self.CountId = 0
        return True

class DaysEntit(BaseEntit):

    def __init__(self):
        super().__init__()
        self.Days: dict[int, Day] = {}

    def add(self, dateId:int, tempId: int):
        count = self.countUp()
        self.Days.update({
            count: Day(count, dateId, tempId)
        })
        return count

    def getAll(self):
        return self.Days
    
    def getById(self, id:int):
        return self.Days.get(id)   
    
    def delete(self, id:int):
        del self.Days[id]
        if not self.Days:
            self.countReset()
        return True
    
    def update(self, id:int, dateId:int, tempId: int):
        self.Days[id].DateId = dateId
        self.Days[id].TempId = tempId
        return True
    
class DatesEntit(BaseEntit):

    def __init__(self):
        super().__init__()
        self.Dates: dict[int, Date] = {}

    def add(self, name:str, d:int, m:int, y:int):
        count = self.countUp()
        self.Dates.update({
            count: Date(count, name, d, m, y)
        })
        return count

    def getAll(self):
        return self.Dates
    
    def getById(self, id:int):
        return self.Dates.get(id)
    
    def delete(self, id:int):
        del self.Dates[id]
        if not self.Dates:
            self.countReset()
        return True
    
    def update(self, id:int, name:str, d:int, m:int, y:int):
        self.Dates[id].Name = name
        self.Dates[id].D = d
        self.Dates[id].M = m
        self.Dates[id].Y = y
        return True
    
class TempsEntit(BaseEntit):
    def __init__(self):
        super().__init__()
        self.Temps: dict[int, Temp] = {}

    def add(self, morn:int, noon:int, night:int):
        count = self.countUp()
        self.Temps.update({
            count: Temp(count, morn, noon, night)
        })
        return count

    def getAll(self):
        return self.Temps
    
    def getById(self, id:int):
        return self.Temps.get(id)   
    
    def delete(self, id:int):
        del self.Temps[id]
        if not self.Temps:
            self.countReset()
        return True
    
    def update(self, id:int, morn:int, noon:int, night:int):
        self.Temps[id].Morn = morn
        self.Temps[id].Noon = noon
        self.Temps[id].Night = night
        return True
    
class WetherDB:

    def __init__(self):
        self.daysE = DaysEntit()
        self.datesE = DatesEntit()
        self.tempsE = TempsEntit()

    def add(self, dto:DTO):
        dateId = self.datesE.add(dto.Name, dto.D, dto.M, dto.Y)
        tempId = self.tempsE.add(dto.Morn, dto.Noon, dto.Night)
        self.daysE.add(dateId, tempId)
        return True

    def getAll(self):
        days = self.daysE.getAll()
        dates = self.datesE.getAll()
        temps = self.tempsE.getAll()
        data = []
        for id in days:
            date = dates[id]
            temp = temps[id]

            data.append({
                "Id": id,
                "Name": date.Name,
                "D" : date.D,
                "M" : date.M,
                "Y" : date.Y,
                "Morn" : temp.Morn,
                "Noon" : temp.Noon,
                "Night" : temp.Night
            })
        return data

    def delete(self, id:int):
        req = self.daysE.getById(id)
        if req == None:
            return None
        self.daysE.delete(id)
        self.datesE.delete(id)
        self.tempsE.delete(id)
        return True
    
    def update(self, dto:DTO):
        req = self.daysE.getById(dto.Id)
        if req == None:
            return None
        self.datesE.update(dto.Id, dto.Name, dto.D, dto.M, dto.Y)
        self.tempsE.update(dto.Id, dto.Morn, dto.Noon, dto.Night)
        return True