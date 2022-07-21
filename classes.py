import streamlit as st
from additional_functions import *

class Spacer:
    def __init__(self):
        None

    def window(self):
        st.write("#")

class Title:
    def __init__(self):
        None

    def window(self):
        st.title("Tvorba receptur pro linku Macchi 1")
        self.col1, self.col2 = st.columns(2)
        product_number = self.col1.text_input("Číslo výrobku:")
        recipe_name = product_number
        self.col2.button("Najdi recept v databázi")
        output_data = [recipe_name, product_number, "----------", "#FALSE#"]

        return output_data

class Details_film:
    def __init__(self):
        None

    def window(self):
        self.col1, self.col2, self.col3 = st.columns(3)
        output_data = []
        output_data.append(self.col1.number_input("Výkon [kg/h]", value=300))
        output_data.append(self.col2.number_input("Šířka [mm]", value=980))
        output_data.append(0)
        output_data.append(self.col3.number_input("Tloušťka [um]", value=85))
        additional_data = [0,0,21,15,125,2,12,125,2,0,0]
        output_data += additional_data
        return output_data

class Details_temperature:
    def __init__(self):
        None

    def window(self):
        options = {"Hostalen F3":"hostalen_temp_regime", "Liten TB49":"liten_temp_regime", "Koextruze":"koex_temp_regime", "Vlastní":"empty"}
        temp_regime = st.radio("Vyberte teplotní režim", options=options.keys(), horizontal=True)
        if temp_regime == "Vlastní":
            return self.new_temp_regime()
        else:
            return self.load_values(options[temp_regime])


    def load_values(self, name):
        with open(name, mode="r") as file:
            data = file.read().splitlines()
            data = list(map(int, data))
            return data

    def new_temp_regime(self):
        self.col1, self.col2, self.col3, self.col4 = st.columns(4)
        temp_regime_list = []
        temp_regime_list.append(self.col1.number_input("A podnásypka [°C]", min_value=0, max_value=300, step=1, value=40))
        temp_regime_list.append(self.col1.number_input("A 1. zóna [°C]", min_value=0, max_value=300, step=1, value=215))
        temp_regime_list.append(self.col1.number_input("A 2. zóna [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col1.number_input("A 3. zóna [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col1.number_input("A 4. zóna [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(0)
        temp_regime_list.append(self.col1.number_input("A sítový blok [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col1.number_input("A krk 1 [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col1.number_input("A krk 2 [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(0)

        temp_regime_list.append(self.col2.number_input("B podnásypka [°C]", min_value=0, max_value=300, step=1, value=40))
        temp_regime_list.append(self.col2.number_input("B 1. zóna [°C]", min_value=0, max_value=300, step=1, value=215))
        temp_regime_list.append(self.col2.number_input("B 2. zóna [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col2.number_input("B 3. zóna [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col2.number_input("B 4. zóna [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col2.number_input("B 5. zóna [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col2.number_input("B sítový blok [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col2.number_input("B krk 1 [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(0)
        temp_regime_list.append(0)

        temp_regime_list.append(self.col3.number_input("C podnásypka [°C]", min_value=0, max_value=300, step=1, value=40))
        temp_regime_list.append(self.col3.number_input("C 1. zóna [°C]", min_value=0, max_value=300, step=1, value=215))
        temp_regime_list.append(self.col3.number_input("C 2. zóna [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col3.number_input("C 3. zóna [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col3.number_input("C 4. zóna [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(0)
        temp_regime_list.append(self.col3.number_input("C sítový blok [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col3.number_input("C krk 1 [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col3.number_input("C krk 2 [°C]", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(0)

        temp_regime_list.append(self.col4.number_input("Hlava 1", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col4.number_input("Hlava 2", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col4.number_input("Hlava 3", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col4.number_input("Hlava 4", min_value=0, max_value=300, step=1, value=230))
        temp_regime_list.append(self.col4.number_input("Hlava 5", min_value=0, max_value=300, step=1, value=230))
        for i in range(93):
            temp_regime_list.append(0)

        return temp_regime_list

class Body:
    def __init__(self):
        self.colA1,\
        self.colA2,\
        self.colA3,\
        self.colB1,\
        self.colB2,\
        self.colB3,\
        self.colC1,\
        self.colC2,\
        self.colC3\
            = st.columns(9)

    def layer_A(self):
        with self.colA1:
            st.text("Procenta A")
            A1p = st.number_input("A1 procenta [%]", min_value=0.0, max_value=100.0, step=0.1, value=100.0)
            A2p = st.number_input("A2 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            A3p = st.number_input("A3 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            A4p = st.number_input("A4 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            A5p = st.number_input("A5 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            A6p = st.number_input("A6 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
        with self.colA2:
            st.text("Název složky A")
            A1l = st.text_input("A1 název")
            A2l = st.text_input("A2 název")
            A3l = st.text_input("A3 název")
            A4l = st.text_input("A4 název")
            A5l = st.text_input("A5 název")
            A6l = st.text_input("A6 název")
            layer_percentage = st.number_input("A layer output [%]", min_value=0, max_value=100, value=25)
        with self.colA3:
            st.text("Hustota složky A")
            A1d = st.number_input("A1 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001, value=0.95)
            A2d = st.number_input("A2 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001)
            A3d = st.number_input("A3 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001)
            A4d = st.number_input("A4 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001)
            A5d = st.number_input("A5 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001)
            A6d = st.number_input("A6 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001)
        return [[A1p, A1l, A1d], [A2p, A2l, A2d], [A3p, A3l, A3d], [A4p, A4l, A4d], [A5p, A5l, A5d],[A6p, A6l, A6d],layer_percentage]

    def layer_B(self):
        with self.colB1:
            st.text("Procenta B")
            B1p = st.number_input("B1 procenta [%]", min_value=0.0, max_value=100.0, step=0.1, value=100.0)
            B2p = st.number_input("B2 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            B3p = st.number_input("B3 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            B4p = st.number_input("B4 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            B5p = st.number_input("B5 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            B6p = st.number_input("B6 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
        with self.colB2:
            st.text("Název složky B")
            B1l = st.text_input("B1 název")
            B2l = st.text_input("B2 název")
            B3l = st.text_input("B3 název")
            B4l = st.text_input("B4 název")
            B5l = st.text_input("B5 název")
            B6l = st.text_input("B6 název")
            layer_percentage = st.number_input("B layer output [%]", min_value=0, max_value=100, value=50)
        with self.colB3:
            st.text("Hustota složky B")
            B1d = st.number_input("B1 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001, value=0.95)
            B2d = st.number_input("B2 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001)
            B3d = st.number_input("B3 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001)
            B4d = st.number_input("B4 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001)
            B5d = st.number_input("B5 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001)
            B6d = st.number_input("B6 hustota [g/Cm3]", min_value=0.0, max_value=10.0, step=0.001)
        return [[B1p, B1l, B1d], [B2p, B2l, B2d], [B3p, B3l, B3d], [B4p, B4l, B4d], [B5p, B5l, B5d],[B6p, B6l, B6d],layer_percentage]

    def layer_C(self):
        with self.colC1:
            st.text("Procenta C")
            C1p = st.number_input("C1 procenta [%]", min_value=0.0, max_value=100.0, step=0.1, value=100.0)
            C2p = st.number_input("C2 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            C3p = st.number_input("C3 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            C4p = st.number_input("C4 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            C5p = st.number_input("C5 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
            C6p = st.number_input("C6 procenta [%]", min_value=0.0, max_value=100.0, step=0.1)
        with self.colC2:
            st.text("Název složky C")
            C1l = st.text_input("C1 název")
            C2l = st.text_input("C2 název")
            C3l = st.text_input("C3 název")
            C4l = st.text_input("C4 název")
            C5l = st.text_input("C5 název")
            C6l = st.text_input("C6 název")
            layer_percentage = st.number_input("C layer output [%]", min_value=0, max_value=100, value=25)
        with self.colC3:
            st.text("Hustota složky C")
            C1d = st.number_input("C1 hustota [g/cm3]", min_value=0.0, max_value=10.0, step=0.001, value=0.95)
            C2d = st.number_input("C2 hustota [g/cm3]", min_value=0.0, max_value=10.0, step=0.001)
            C3d = st.number_input("C3 hustota [g/cm3]", min_value=0.0, max_value=10.0, step=0.001)
            C4d = st.number_input("C4 hustota [g/cm3]", min_value=0.0, max_value=10.0, step=0.001)
            C5d = st.number_input("C5 hustota [g/cm3]", min_value=0.0, max_value=10.0, step=0.001)
            C6d = st.number_input("C6 hustota [g/cm3]", min_value=0.0, max_value=10.0, step=0.001)
        return [[C1p, C1l, C1d],[C2p, C2l, C2d],[C3p, C3l, C3d],[C4p, C4l, C4d],[C5p, C5l, C5d],[C6p, C6l, C6d],layer_percentage]


    def window(self):
        layer_A = Layer("A", self.layer_A())
        layer_B = Layer("B", self.layer_B())
        layer_C = Layer("C", self.layer_C())

        dosing_output = [layer_A.get_dosing_output(), layer_B.get_dosing_output(), layer_C.get_dosing_output()]
        text_output = [layer_A.get_text_output(), layer_B.get_text_output(), layer_C.get_text_output()]
        density_output = [layer_A.get_density_output(), layer_B.get_density_output(), layer_C.get_density_output()]

        layer_percentage = [layer_A.get_layer_percentage(), layer_B.get_layer_percentage(), layer_C.get_layer_percentage()]

        layer_density_output = [layer_A.get_layer_density(), layer_B.get_layer_density(), layer_C.get_layer_density()]

        final_output = {}

        final_output["dosing_output"] = dosing_output
        final_output["text_output"] = text_output
        final_output["density_output"] = density_output
        final_output["layer_density_output"] = layer_density_output
        final_output["layer_percentage"] = layer_percentage

        return final_output

class Layer:
    def __init__(self, label, table):
        self.label = label
        self.table = table

    def get_dosing_output(self):
        formated_output = [self.table[0][0], self.table[1][0], self.table[2][0], self.table[3][0], self.table[4][0], self.table[5][0]]
        return formated_output

    def get_text_output(self):
        formated_output = [str(self.table[0][1]), str(self.table[1][1]), str(self.table[2][1]), str(self.table[3][1]), str(self.table[4][1]) , str(self.table[5][1])]
        return formated_output

    def get_density_output(self):
        formated_output = [self.table[0][2], self.table[1][2], self.table[2][2], self.table[3][2], self.table[4][2], self.table[5][2]]
        return formated_output

    def get_layer_density(self):
        layer_density = 0
        for i in self.table:
            try:
                layer_density += i[0]*i[2]*0.01
            except:
                None
        return layer_density

    def get_layer_percentage(self):
        return self.table[6]

def gui():
    st.set_page_config(layout="wide")
    data_from_gui = {}

    free_space = Spacer()

    title = Title()
    title_data = title.window()
    data_from_gui["title_data"] = title_data

    free_space.window()

    parameters = Details_film()
    film_data = parameters.window()
    data_from_gui["film_data"] = film_data

    free_space.window()

    temp_regime = Details_temperature()
    temp_data = temp_regime.window()
    data_from_gui["temp_data"] = temp_data

    free_space.window()

    dosing = Body()
    dosing_data = dosing.window()
    data_from_gui["dosing_data"] = dosing_data

    return data_from_gui

def constructor(data_from_gui):
    title = data_from_gui['title_data']
    film_data = data_from_gui['film_data']
    temp_data = data_from_gui['temp_data']
    density_per_layer_data = data_from_gui['dosing_data']['layer_density_output']
    percentage_per_layer_data = data_from_gui['dosing_data']['layer_percentage']
    dosing_data = data_from_gui['dosing_data']['dosing_output']
    dosing_text_data = data_from_gui['dosing_data']['text_output']
    density_data = data_from_gui['dosing_data']['density_output']
    text_dosing_filler = filler(54, 'text')
    number_dosing_filler = filler(54, 'zero')

    thickness = film_data[3]
    throughput = film_data[0]
    width = film_data[1]
    name = title[0]

    thickness_per_layer = percentage_calculator(thickness, percentage_per_layer_data)
    throughput_per_layer = percentage_calculator(throughput, percentage_per_layer_data)

    density_percentage_output = alternating_merge(density_per_layer_data, percentage_per_layer_data) + filler(34, 'zero')
    thickness_throughput_output = alternating_merge(thickness_per_layer, throughput_per_layer) + filler(19, 'zero')

    title_output = list_to_string(title)
    temp_output = list_to_string(temp_data)
    film_output = list_to_string(film_data) + "\n" + list_to_string(density_percentage_output) + "\n" + list_to_string(thickness_throughput_output)
    draw_speed = str(line_speed(percentage_per_layer_data, thickness, throughput, density_per_layer_data, width))
    A_dosing = list_to_string(dosing_data[0])
    B_dosing = list_to_string(dosing_data[1])
    C_dosing = list_to_string(dosing_data[2])
    dosing_filler = list_to_string(filler(42, 'zero'))
    A_text = list_to_string(dosing_text_data[0])
    B_text = list_to_string(dosing_text_data[1])
    C_text = list_to_string(dosing_text_data[2])
    text_filler = list_to_string(filler(146, 'text'))
    A_density = list_to_string(density_data[0])
    B_density = list_to_string(density_data[1])
    C_density = list_to_string(density_data[2])
    density_filler = list_to_string(filler(36, 'zero'))
    mfi_filler = list_to_string(filler(54, 'zero'))
    end_filler = list_to_string(filler(54, 'text'))

    final_output = title_output + "\n" + \
        temp_output + "\n" + \
        film_output + "\n" + \
        draw_speed + "\n" + \
        A_dosing + "\n" + B_dosing + "\n" + C_dosing + "\n" + \
        dosing_filler + "\n" + \
        A_text + B_text + C_text + "\n" + \
        text_filler + "\n" + \
        mfi_filler + "\n" + \
        A_density + "\n" + B_density + "\n" + C_density + "\n" + \
        density_filler + "\n" + \
        end_filler

    return [final_output, name]

def writer(data, name):
    caption = name + '.rcp'
    with open(caption, mode='w+') as file:
        file.write(data)




