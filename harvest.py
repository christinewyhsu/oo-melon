############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        if type(pairing) == str:
            self.pairings.append(pairing)
        else:
            self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    # Class MelonType params: code, first_harvest, color, is_seedless, is_bestseller, name)
    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")

    casaba = MelonType("cas", 2003, "orange", False, None, "Casaba")
    casaba.add_pairing(["strawberries", "mint"])

    crenshaw = MelonType("cren", 2003, "green", False, None, "Crenshaw")
    crenshaw.add_pairing("prosciutto")

    watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    watermelon.add_pairing("ice cream")

    all_melon_types = [musk, casaba, crenshaw, watermelon]

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        name = melon_type.name
        pairings = melon_type.pairings

        print(f'{melon_type.name} pairs with')
        for pair in pairings:
            print(f'- {pair}')
        
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # code, first_harvest, color, is_seedless, is_bestseller, name)
    # keys = codes
    # values = instances of MelonType class
    melon_dict = {}
    for melon in melon_types:
        code = melon.code
        # Be sure to set the value of the melon_type to be an instance of MelonType (not a string)
        melon_dict[code] = melon
    
    return melon_dict
    

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field_id, harvestor_name):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_id = field_id
        self.harvestor_name = harvestor_name

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field_id != 3:
            return True
        return False


def make_melons():
    """Returns a list of Melon objects."""

    # Instantiate Class Melon for each melon listed
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    # Create melons_list
    melons_list = list(map(eval, ['melon_' + str(index) for index in range(1,10)]))
    
    return melons_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    # melon_type, shape_rating, color_rating, field_id, harvestor_name
    for melon in melons:
        harvestor_name = melon.harvestor_name
        field_id = melon.field_id
        sellable = melon.is_sellable()
        print(f'Harvested by {harvestor_name} from Field {field_id} {"(CAN BE SOLD)" if sellable else "(NOT SELLABLE)"}')


def read_file(filepath):
    
    with open(filepath) as input_file:
        melons_list = []
        for line in input_file:

            # Splits the items in the line
            line = line.rsplit() #['Shape', '4', 'Color', '2', 'Type', 'yw', 'Harvested', 'By', 'Sheila', 'Field', '#', '55']

            # Parses the line
            for index, item in enumerate(line):
                if item == 'Shape':
                    shape_rating = int(line[index+1])
                elif item == 'Color':
                    color_rating = int(line[index+1])
                elif item == 'Type':
                    melon_code = line[index+1]
                elif item == 'By':
                    harvestor_name = line[index+1]
                elif item == '#':
                    field_id = int(line[index+1])

            # Create Melon Object
            # class Melon params: melon_type, shape_rating, color_rating, field_id, harvestor_name)
            curr_melon = Melon(melons_by_id[melon_code], shape_rating, color_rating, field_id, harvestor_name)

            melons_list.append(curr_melon)
    
    return melons_list


if __name__ == '__main__':
    melon_types = make_melon_types()
    print_pairing_info(melon_types)
    melons_by_id = make_melon_type_lookup(melon_types)
    melons_list = make_melons()
    get_sellability_report(melons_list)
    report = read_file('harvest_log.txt')