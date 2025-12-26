from datetime import date    # This was added for the death_date and birth_date to show exact ages

class Person: # A person class is made which contain the name, birthdate and death date with a null because some people are still alive and makes the code simpler
    def __init__(self, name, birth_date, death_date=None):
        self.name = name
        self.birth_date = birth_date
        self.death_date = death_date
        self.parents = []
        self.children = []
        self.partners = []
        self.grandchildren = [] # Empty lists are made for parents, children, partners and grandchildren to add the family information
        self.immediate_families = []
        self.extended_families = []
        self.siblings = []
        self.cousins = []



    def add_child(self, child):
        if child not in self.children: # Makes sure the same child is not repeatedly added
            self.children.append(child) # This adds the child to the children list of parents to establish parent to child relationship
            child.parents.append(self) # This adds the child to the children list of parents to establish child to parent relationship

    def add_parent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)
            parent.children.append(self) # Same as the previous ones but with parents

    def add_grandchild(self, grandchild):
        if grandchild not in self.grandchildren:
            self.grandchildren.append(grandchild) # There's no reverse because if someone Rafi's grandchild is Anabella it doesn't mean Anabella's grandchild is Rafi

    def add_immediate_family(self, immediate_family):
        if immediate_family not in self.immediate_families:
            self.immediate_families.append(immediate_family)
            immediate_family.immediate_families.append(self) # Same as the previous ones but with immediate_family

    def add_extended_family(self, extended_family):
        if extended_family not in self.extended_families:
            self.extended_families.append(extended_family)
            extended_family.extended_families.append(self)

    def add_sibling(self, sibling):
        if sibling not in self.siblings:
            self.siblings.append(sibling)
            sibling.siblings.append(self)

    def add_cousin(self, cousin):
        if cousin not in self.cousins:
            self.cousins.append(cousin)
            cousin.cousins.append(self)


class FamilyTree: # This is where Person is stored to add to the family tree
    def __init__(self):
        self.members = [] # List to add family members

    def add_member(self, person):
        if person not in self.members:
            self.members.append(person) # This is to add members to the family tree


    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member # This is for the user to request a family member and the code to find them
        return None

    def display_parents(self, name):
        person= self.find_member(name)
        if person:
            print("Parents of " + person.name + ":")
            if person.parents:
                for parent in person.parents:
                    print(parent.name)
            else:
                print(person.name + " has no parents listed in the family tree.")
        else:
            print("No person named" + name + "found in the family tree.")

    def display_grandchildren(self, name):
        person= self.find_member(name)
        if person:
            print("Grandchildren of " + person.name + ":")
            if person.grandchildren:
                for grandchild in person.grandchildren:
                    print(grandchild.name)
            else:
                print(person.name + " has no grandchildren listed in the family tree.")
        else:
            print("No person named" + name + "found in the family tree.")

    def display_immediate_families(self, name):
        person= self.find_member(name)
        if person:
            print("The immediate family of " + person.name + "is :")
            if person.immediate_families:
                for immediate_family in person.immediate_families:
                    print(immediate_family.name)
            else:
                print(person.name + "has no immediate family listed in the family tree.")
        else:
            print("No person named" + name + "found in the family tree.")

    def display_extended_families(self, name):
        person= self.find_member(name)
        if person:
            print("The extended family of " + person.name + "is :")
            if person.extended_families:
                for extended_family in person.extended_families:
                    print(extended_family.name)
            else:
                print(person.name + "has no extended family listed in the family tree.")
        else:
            print("No person named" + name + "found in the family tree.")

    def display_siblings(self, name):
        person= self.find_member(name)
        if person:
            print("The siblings/sibling of " + person.name + "are/is :")
            if person.siblings:
                for sibling in person.siblings:
                    print(sibling.name)
            else:
                print(person.name + "has no sibling/siblings family listed in the family tree.")
        else:
            print("No person named" + name + "found in the family tree.")

    def display_cousins(self, name):
        person= self.find_member(name)
        if person:
            print("The cousin/cousins of " + person.name + "is/are :")
            if person.cousins:
                for cousin in person.cousins:
                    print(cousin.name)
            else:
                print(person.name + "has no cousin/cousins listed in the family tree.")
        else:
            print("No person named" + name + "found in the family tree.")


    def display_birth_date(self):
        print("List of Family Birthdays:")
        for person in self.members:
            if person.birth_date:
                print(person.name + " -> " , person.birth_date )

    def display_sorted_birth_date(self):
        print("List of Family Birthdays (sorted by date):")
        birthday_dict = {} # Creates a dictionary
        for person in self.members:
            if person.birth_date:
                birthday = person.birth_date.strftime("%m-%d") # Makes month and date become a string
                if birthday not in birthday_dict:
                    birthday_dict[birthday] = []
                birthday_dict[birthday].append(person.name)
        for birthday in sorted(birthday_dict.keys()): # Sorts the birthday by month and day format
            names = ', '.join(birthday_dict[birthday])
            print(birthday , " -> " , names)

    def display_children(self, name):
        person= self.find_member(name)
        if person:
            print("The child/children of " + person.name + "is/are :")
            if person.children:
                for child in person.children:
                    print(child.name)
            else:
                print(person.name + "has no child/children listed in the family tree.")
        else:
            print("No person named" + name + "found in the family tree.")


class FamilyTree_Stats:
    def __init__(self, family_tree):
        self.family_tree = family_tree


    def average_Age_Of_Death(self):
        total_age = 0
        count = 0

        for person in self.family_tree.members:
            if person.birth_date and person.death_date:
                age_at_death = person.death_date.year - person.birth_date.year
                if (person.death_date.month, person.death_date.day) < (person.birth_date.month, person.birth_date.day):
                    age_at_death -=1
                total_age += age_at_death
                count += 1

        if count == 0:
            print("No data to calculate average death age")
        else:
            average_age = total_age / count
            print("Average age at death", round(average_age, 2), "years")

    def children_per_person(self):
        children_counts = {}
        for person in self.family_tree.members:
            children_counts[person.name] = len(person.children)
        print("Number of children per person:")
        for name, count in children_counts.items():
            print(name , ":" , count , "children")
        return children_counts

    def average_children_per_person(self):
        total_children = 0
        total_people = len(self.family_tree.members)
        for person in self.family_tree.members:
            total_children += len(person.children)
        if total_people == 0:
            print("No people in the family tree.")
            return None
        else:
            average_children = total_children / total_people
            print("Average number of children per person:")
            print(round(average_children, 2))
            return average_children


# Main program


family_tree = FamilyTree() # Starts an empty family to add members
family_tree_stats = FamilyTree_Stats(family_tree)

Rafi = Person("Rafi Uddin", date(1947, 6, 18), date(2020, 3, 12))
Fatima = Person("Fatima Uddin", date(1948, 12, 1))
Harry = Person("Harry Uddin", date(1970, 3, 7))
Lana = Person("Lana Uddin", date(1972, 4, 19))
Anabella = Person("Anabella Uddin", date(2000, 8, 18))
Max = Person("Max Uddin", date(2003, 5, 5))
Emma = Person("Emma Torres", date(1973, 8, 23))
Felipe = Person("Felipe Torres", date(1971, 12, 13))
Zara = Person("Zara Torres", date(2005, 6, 11))
Davier = Person("Davier Uddin", date(1950, 5, 13), date(2015, 2, 28))

Javier = Person("Javier Torres", date(1940, 4, 29), date(2000, 10, 2))
Carla = Person("Carla Torres", date(1945, 3, 16), date(2001, 4, 16))
Sofia = Person("Sofia Torres", date(1973, 12, 1))
Jose = Person("Jose Torres", date(1975, 11, 22))
Violet = Person("Violet Torres", date(1973, 6, 13))
Paula = Person("Paula Torres", date(2005, 4, 8))
Francisco = Person("Francisco Torres", date(1946, 2, 21), date(2016, 7, 15))
Maria = Person("Maria Torres", date(1950, 6, 19))
Ivan = Person("Ivan Torres", date(1974, 4, 27))
Cristina = Person("Cristina Torres", date(1977, 8, 19))



Rafi_grandchildren = [Anabella, Max, Zara]
for grandchild in Rafi_grandchildren:
    Rafi.add_grandchild(grandchild)

Rafi_immediate_family = [Davier, Fatima, Emma, Harry]
for member in Rafi_immediate_family:
    Rafi.add_immediate_family(member)

Rafi_extended_family = [Davier, Fatima, Emma, Harry]
for member in Rafi_extended_family:
    Rafi.add_extended_family(member)

Rafi_sibling = [Davier]
for member in Rafi_sibling:
    Rafi.add_sibling(member)

Rafi_cousin = []
for member in Rafi_cousin:
    Rafi.add_cousin(member)

Rafi_child = []
for member in Rafi_child:
    Rafi.add_child(member)


Fatima_grandchildren = [Anabella, Max, Zara]
for grandchild in Fatima_grandchildren:
    Fatima.add_grandchild(grandchild)

Fatima_immediate_family = [Harry, Emma]
for member in Fatima_immediate_family:
    Fatima.add_immediate_family(member)

Fatima_extended_family = [Harry, Emma]
for member in Fatima_extended_family:
    Fatima.add_extended_family(member)

Fatima_sibling = []
for member in Fatima_sibling:
    Fatima.add_sibling(member)

Fatima_cousin = []
for member in Fatima_cousin:
    Fatima.add_cousin(member)



Harry_parents = [Rafi, Fatima]
for parent in Harry_parents:
    Harry.add_parent(parent)

Harry_immediate_family = [Lana, Anabella, Max, Emma]
for member in Harry_immediate_family:
    Harry.add_immediate_family(member)

Harry_extended_family = [Lana, Anabella, Max, Emma, Davier]
for member in Harry_extended_family:
    Harry.add_extended_family(member)

Harry_sibling = [Emma]
for member in Harry_sibling:
    Harry.add_sibling(member)

Harry_cousin = []
for member in Harry_cousin:
    Harry.add_cousin(member)



Lana_immediate_family = [Anabella, Max]
for member in Lana_immediate_family:
    Lana.add_immediate_family(member)

Lana_extended_family = [Anabella, Max]
for member in Lana_extended_family:
    Lana.add_extended_family(member)

Lana_sibling = []
for member in Lana_sibling:
    Lana.add_sibling(member)

Lana_cousin = []
for member in Lana_cousin:
    Lana.add_cousin(member)



Anabella_parents = [Harry, Lana]
for parent in Anabella_parents:
    Anabella.add_parent(parent)

Anabella_immediate_family = [Max]
for member in Anabella_immediate_family:
    Anabella.add_immediate_family(member)

Anabella_extended_family = [Max, Emma, Felipe, Zara]
for member in Anabella_extended_family:
    Anabella.add_extended_family(member)

Anabella_sibling = [Max]
for member in Anabella_sibling:
    Anabella.add_sibling(member)

Anabella_cousin = [Zara]
for member in Anabella_cousin:
    Anabella.add_cousin(member)



Max_parents = [Harry, Lana]
for parent in Max_parents:
    Max.add_parent(parent)

Max_extended_family = [Emma, Felipe, Zara]
for member in Max_extended_family:
    Max.add_extended_family(member)

Max_sibling = []
for member in Max_sibling:
    Max.add_sibling(member)

Max_cousin = [Zara]
for member in Max_cousin:
    Max.add_cousin(member)



Emma_parents = [Rafi, Fatima]
for parent in Emma_parents:
    Emma.add_parent(parent)

Emma_immediate_family = [Felipe, Zara]
for member in Emma_immediate_family:
    Emma.add_immediate_family(member)

Emma_extended_family = [Felipe, Zara, Davier, Francisco, Maria, Ivan, Cristina]
for member in Emma_extended_family:
    Emma.add_extended_family(member)

Emma_sibling = []
for member in Emma_sibling:
    Emma.add_sibling(member)

Emma_cousin = []
for member in Emma_cousin:
    Emma.add_cousin(member)



Felipe_parents = [Javier, Carla]
for parent in Felipe_parents:
    Felipe.add_parent(parent)

Felipe_immediate_family = [Zara, Javier, Carla, Sofia, Jose]
for member in Felipe_immediate_family:
    Felipe.add_immediate_family(member)

Felipe_extended_family = [Zara, Javier, Carla, Sofia, Jose, Francisco, Maria, Ivan, Cristina, Davier]
for member in Felipe_extended_family:
    Felipe.add_extended_family(member)

Felipe_sibling = [Sofia, Jose]
for member in Felipe_sibling:
    Felipe.add_sibling(member)

Felipe_cousin = [Ivan, Cristina]
for member in Felipe_cousin:
    Felipe.add_cousin(member)



Zara_parents = [Emma, Felipe]
for parent in Zara_parents:
    Zara.add_parent(parent)

Zara_extended_family = [Sofia, Jose, Violet, Paula]
for member in Zara_extended_family:
    Zara.add_extended_family(member)

Zara_sibling = []
for member in Zara_sibling:
    Zara.add_sibling(member)

Zara_cousin = [Paula]
for member in Zara_cousin:
    Zara.add_cousin(member)



Javier_grandchildren = [Paula]
for grandchild in Javier_grandchildren:
    Javier.add_grandchild(grandchild)

Javier_immediate_family = [Carla, Sofia, Jose, Francisco]
for member in Javier_immediate_family:
    Javier.add_immediate_family(member)

Javier_extended_family = [Carla, Sofia, Jose, Francisco]
for member in Javier_extended_family:
    Javier.add_extended_family(member)

Javier_sibling = [Francisco]
for member in Javier_sibling:
    Javier.add_sibling(member)

Javier_cousin = []
for member in Javier_cousin:
    Javier.add_cousin(member)



Carla_grandchildren = [Paula]
for grandchild in Carla_grandchildren:
    Carla.add_grandchild(grandchild)

Carla_immediate_family = [Sofia, Jose]
for member in Carla_immediate_family:
    Carla.add_immediate_family(member)

Carla_extended_family = [Sofia, Jose]
for member in Carla_extended_family:
    Carla.add_extended_family(member)

Carla_sibling = []
for member in Carla_sibling:
    Carla.add_sibling(member)

Carla_cousin = []
for member in Carla_cousin:
    Carla.add_cousin(member)



Sofia_parents = [Javier, Carla]
for parent in Sofia_parents:
    Sofia.add_parent(parent)

Sofia_immediate_family = [Jose]
for member in Sofia_immediate_family:
    Sofia.add_immediate_family(member)

Sofia_extended_family = [Jose, Francisco, Maria]
for member in Sofia_extended_family:
    Sofia.add_extended_family(member)

Sofia_sibling = [Jose]
for member in Sofia_sibling:
    Sofia.add_sibling(member)

Sofia_cousin = [Ivan, Cristina]
for member in Sofia_cousin:
    Sofia.add_cousin(member)



Jose_parents = [Javier, Carla]
for parent in Jose_parents:
    Jose.add_parent(parent)

Jose_immediate_family = [Violet, Paula]
for member in Jose_immediate_family:
    Jose.add_immediate_family(member)

Jose_extended_family = [Violet, Paula, Francisco, Maria]
for member in Jose_extended_family:
    Jose.add_extended_family(member)

Jose_sibling = []
for member in Jose_sibling:
    Jose.add_sibling(member)

Jose_cousin = [Ivan, Cristina]
for member in Jose_cousin:
    Jose.add_cousin(member)



Violet_immediate_family = [Paula]
for member in Violet_immediate_family:
    Violet.add_immediate_family(member)

Violet_extended_family = [Paula, Francisco, Maria]
for member in Violet_extended_family:
    Violet.add_extended_family(member)

Violet_sibling = []
for member in Violet_sibling:
    Violet.add_sibling(member)

Violet_cousin = []
for member in Violet_cousin:
    Violet.add_cousin(member)



Paula_parents = [Violet, Jose]
for parent in Paula_parents:
    Paula.add_parent(parent)

Paula_extended_family = [Sofia, Felipe, Zara, Emma]
for member in Paula_extended_family:
    Paula.add_extended_family(member)

Paula_sibling = []
for member in Paula_sibling:
    Paula.add_sibling(member)

Paula_cousin = [Zara]
for member in Paula_cousin:
    Paula.add_cousin(member)



Francisco_immediate_family = [Maria, Ivan, Cristina]
for member in Francisco_immediate_family:
    Francisco.add_immediate_family(member)

Francisco_extended_family = [Maria, Ivan, Cristina]
for member in Francisco_extended_family:
    Francisco.add_extended_family(member)

Francisco_sibling = []
for member in Francisco_sibling:
    Francisco.add_sibling(member)

Francisco_cousin = []
for member in Francisco_cousin:
    Francisco.add_cousin(member)



Maria_immediate_family = [Ivan, Cristina]
for member in Maria_immediate_family:
    Maria.add_immediate_family(member)

Maria_extended_family = [Ivan, Cristina]
for member in Maria_extended_family:
    Maria.add_extended_family(member)

Maria_sibling = []
for member in Maria_sibling:
    Maria.add_sibling(member)

Maria_cousin = []
for member in Maria_cousin:
    Maria.add_cousin(member)



Ivan_parents = [Francisco, Maria]
for parent in Ivan_parents:
    Ivan.add_parent(parent)

Ivan_immediate_family = [Cristina]
for member in Ivan_immediate_family:
    Ivan.add_immediate_family(member)

Ivan_extended_family = [Cristina, Sofia, Jose, Felipe, Emma, Violet]
for member in Ivan_extended_family:
    Ivan.add_extended_family(member)

Ivan_sibling = [Cristina]
for member in Ivan_sibling:
    Ivan.add_sibling(member)

Ivan_cousin = []
for member in Ivan_cousin:
    Ivan.add_cousin(member)



Cristina_parents = [Francisco, Maria]
for parent in Cristina_parents:
    Cristina.add_parent(parent)

Cristina_extended_family = [Sofia, Jose, Felipe, Emma, Violet]
for member in Cristina_extended_family:
    Cristina.add_extended_family(member)

Cristina_sibling = []
for member in Cristina_sibling:
    Cristina.add_sibling(member)

Cristina_cousin = []
for member in Cristina_cousin:
    Cristina.add_cousin(member)




uddin_and_torres_members = [Rafi, Fatima, Harry, Lana, Anabella, Max, Emma, Felipe, Zara, Davier, Javier, Carla, Sofia, Jose, Violet, Paula, Francisco, Maria, Ivan, Cristina]

for member in uddin_and_torres_members:
    family_tree.add_member(member) # Add all the members to the family tree using the add_member method implemented before

    # The menu system
while True:# This is to keep the menu open after the user input and not have to constantly run the code to use it till the user exits
    print("Family Tree Menu:")
    print("1. Display parents")
    print("2. Display grandchildren")
    print("3. Display immediate family")
    print("4. Display extended family")
    print("5. Display siblings")
    print("6. Display cousins")
    print("7. Display list of family birthdays")
    print("8. Display birthday calendar")
    print("9. display average age at death ")
    print("10.Display number of children for each person")
    print("11. Display average number of children per person")
    print("12. End")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the name of the person")
        family_tree.display_parents(name)
        pass
    elif choice == '2':
        name = input("Enter the name of the person")
        family_tree.display_grandchildren(name)
        pass
    elif choice == '3':
        name = input("Enter the name of the person")
        family_tree.display_immediate_families(name)
        pass
    elif choice == '4':
        name = input("Enter the name of the person")
        family_tree.display_extended_families(name)
        pass
    elif choice == '5':
        name = input("Enter the name of the person")
        family_tree.display_siblings(name)
        pass
    elif choice == '6':
        name = input("Enter the name of the person")
        family_tree.display_cousins(name)
        pass
    elif choice == '7':
        family_tree.display_birth_date()
        pass
    elif choice == '8':
        family_tree.display_sorted_birth_date()
        pass
    elif choice == '9':
        family_tree_stats.average_Age_Of_Death()
        pass
    elif choice == '10':
        family_tree_stats.children_per_person()
        pass
    elif choice == '11':
        family_tree_stats.average_children_per_person()
        pass
    elif choice =='12':
        break