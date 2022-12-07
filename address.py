# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/12/06
# Gets user information on their mailing address then uses a
# function to format the address. Uses a default to check if
# the user lives in an apartment

# Function to format the mailing address of the user
def format_mailing_address(
    name, street_num, street, city, province, postal_code, apartment_num
):
    mailing_address = ""
    # The format if they live in an apartment
    if apartment_num != None:
        mailing_address = (
            name
            + "\n"
            + apartment_num
            + "-"
            + street_num
            + " "
            + street
            + "\n"
            + city
            + " "
            + province
            + " "
            + postal_code
        )

    # The format if they do not live in an apartment
    else:
        mailing_address = (
            name
            + "\n"
            + street_num
            + " "
            + street
            + "\n"
            + city
            + " "
            + province
            + " "
            + postal_code
        )

    # Return the formatting
    return mailing_address.upper()


def main():

    # Title of the program
    print("Mailing address\n")
    user_apartment = None

    # User input for their name and whether they have an apartment
    user_name = input("Please enter your name: ")
    user_apartment_ask = input("Do you have an apartment?(y/yes/n/no): ")

    # If they have an apartment, ask for their apartment number
    if user_apartment_ask.upper() == "Y" or user_apartment_ask.upper() == "YES":
        user_apartment = input("Enter your apartment number: ")

    # the rest of the inputs
    user_street_num = input("Enter your street number: ")
    user_street_name = input("Enter your street name: ")
    user_city = input("Enter your city: ")
    user_province = input("Enter your province: ")
    user_postal_code = input("Enter your postal code: ")

    # To call the function and get a return value
    mailing_address = format_mailing_address(
        user_name,
        user_street_num,
        user_street_name,
        user_city,
        user_province,
        user_postal_code,
        user_apartment,
    )

    # Print the mailing address
    print("Your mailing address is: \n")
    print(mailing_address)


if __name__ == "__main__":
    main()
