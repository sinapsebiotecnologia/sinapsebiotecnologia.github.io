import streamlit as st
import pandas
import pip
pip.main(["install", "openpyxl"])

def main():

    excel_data_df = pandas.read_excel('teste.xlsx')
    json_str = excel_data_df.to_json()
    if json_str != "None":
        with open("teste.json", "w") as arquivo:
            arquivo.write(json_str)


if __name__ == '__main__':
    main()