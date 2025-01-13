import random

# Stockage global
all_products = [
    {
        'sku': '89',
        'name': '89',
        'description': '89'
    },
    {
        'sku': '88',
        'name': '88',
        'description': '88'
    }
]
all_hierarchies = [
    {
        'id': 1,
        'name': '89'
    }
]
all_relations = [
    {
        'id': 1,
        'product_sku': ['89', '88'],
        'hierarchy_id': 1
    }
]


# =========================
# CLASSES
# =========================
class Product:
    def __init__(self, sku, name, description):
        self.sku = self._string_verification(sku)
        self.name = self._string_verification(name)
        self.description = self._string_verification(description)

    @staticmethod
    def _string_verification(value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("ERROR: The value must be a non-empty string.")
        return value


class Hierarchy:
    def __init__(self, name):
        self.name = name
        self.id = self.generate_id()

    @staticmethod
    def generate_id():
        return random.randint(1, 300)


# =========================
# FONCTIONS PRINCIPALES
# =========================
def pim_logic():
    """Fonction principale du PIM System."""
    print("Welcome to your PIM System!")
    while True:
        user_choice = input("Please select an action: \n'P' to create a product\n'H' to create a hierarchy"
                            "\n'DP' to display all products\n'DH' to display all hierarchies\n'DR' to make "
                            "relations\n"
                            "'PR' to print all the relations\n'"
                            "'Q' "
                            "to quit: ").upper()
        if user_choice == 'P':
            create_product()
        elif user_choice == 'H':
            create_hierarchy()
        elif user_choice == 'DP':
            display_all_products()
        elif user_choice == 'DH':
            display_all_hierarchies()
        elif user_choice == 'DR':
            make_relation()
        elif user_choice == 'PR':
            display_relations(all_relations)
        elif user_choice == 'Q':
            print("Thank you for using the PIM system. See you soon!")
            break
        else:
            print("Invalid input. Please try again.")


def create_product():
    """Créer un produit."""
    print("\nLet's create a new product!")
    sku = check_if_empty(input("Enter SKU: "))
    name = check_if_empty(input("Enter Name: "))
    description = check_if_empty(input("Enter Description: "))

    new_product = Product(sku, name, description)
    all_products.append(new_product.__dict__)
    print(all_products)
    print("\n✅ Product created successfully!")
    display_all_products()


def create_hierarchy():
    """Créer une hiérarchie."""
    print("\nLet's create a new hierarchy!")
    name = check_if_empty(input("Enter Hierarchy Name: "))

    new_hierarchy = Hierarchy(name)
    all_hierarchies.append(new_hierarchy.__dict__)
    print(all_hierarchies)

    print("\n✅ Hierarchy created successfully!")
    display_all_hierarchies()


def display_all_products():
    """Afficher tous les produits."""
    if not all_products:
        print("\nNo products found.")
        return

    print("\nBelow is the list of all your products:")
    print('-' * 30)
    for product in all_products:
        print(f"SKU: {product['sku']}")
        print(f"Name: {product['name']}")
        print(f"Description: {product['description']}")
        print('-' * 30)


def display_all_hierarchies():
    """Afficher toutes les hiérarchies."""
    if not all_hierarchies:
        print("\nNo hierarchies found.")
        return

    print("\nBelow is the list of all your hierarchies:")
    print('-' * 30)
    for hierarchy in all_hierarchies:
        print(f"ID: {hierarchy['id']}")
        print(f"Name: {hierarchy['name']}")
        print('-' * 30)


def make_relation():
    RELATION_ID = random.randint(0, 1000)
    display_all_products()
    display_all_hierarchies()
    while len(all_products) == 0 and len(all_hierarchies) == 0:
        print('You need to create at list one product and one hierarchy')
        pim_logic()
    else:
        user_product_selection = get_valid_value_in_list(all_products, 'Product', 'sku')
        user_hiearchy_selection = get_valid_value_in_list(all_hierarchies, 'Hierarchy', 'id')

        new_relation = {
            'id': RELATION_ID,
            'product_sku': [user_product_selection],
            'hierarchy_id': user_hiearchy_selection['id']
        }

        for relation in all_relations:
            ind = 0
            if relation['product_sku'] is not None and new_relation['product_sku'][ind]['sku'] in relation['product_sku'] \
                    and \
                    new_relation['hierarchy_id'] == relation['hierarchy_id']:
                print("ERROR, the relation is already in our database, you cannot assign twice the same product SKU "
                      "to one hierarchy")
                print(all_relations)
                ind += 1
            elif new_relation['hierarchy_id'] == relation['hierarchy_id']:
                print("\n✅ Product added successfully to the hierarchy {}!!!".format(relation['hierarchy_id']))
                print(new_relation['product_sku'][0]['sku'])
                relation['product_sku'].append(new_relation['product_sku'][0]['sku'])
                print(all_relations)
                break
            else:
                all_relations.append(new_relation)
                break


def display_relations(all_relations):
    print(all_relations)
    nbr_dots = 10
    for relation in all_relations:
        print("-" * 30)
        print("Below the list of the products included in the hierarchy ID {}".format(relation['hierarchy_id']))
        for product in relation['product_sku']:
            print('-' * nbr_dots, '>', product)
            nbr_dots += 10


# =========================
# FONCTIONS UTILITAIRES
# =========================
def check_if_empty(value):
    """Vérifier que la valeur entrée n'est pas vide."""
    while not value.strip():
        value = input("Empty value is not allowed. Please try again: ")
    return value


def get_valid_value_in_list(lst, search_value, dict_term):
    while True and search_value != 'Hierarchy':
        user_value_selection = input(f'Please choose a {search_value}: ')
        value = next((p for p in lst if p[dict_term] == user_value_selection), None)
        if value:
            return value
        print('Invalid SKU or ID. Please try again.')
    else:
        user_value_selection = input(f'Please choose a {search_value}: ')
        value = next((p for p in lst if p[dict_term] == int(user_value_selection)), None)
        if value:
            return value
        print('Invalid SKU or ID. Please try again.')


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    pim_logic()