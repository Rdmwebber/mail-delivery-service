# Mail Delivery Service

This repository contains a Python-based application that simulates a mail delivery service. The project uses a hash map for efficient data storage and retrieval, and a graph-based approach to determine the most optimal routes for package delivery.

## Features

* **Efficient Data Storage:** Utilizes a hash map (`hash_map.py`) to store and access package information quickly.

* **Optimal Route Calculation:** Implements the **Nearest Neighbour Optimization Heuristic** algorithm to determine the most efficient delivery routes for multiple trucks.

* **Package and Truck Management:** Manages packages and trucks as objects, each with their own attributes and functionalities.

* **Data Loading:** Loads package and address data from external CSV files.

## Technologies Used

* Python 3

## File Structure

* `main.py`: The entry point of the application. It orchestrates the loading of data, the management of trucks, and the delivery process.

* `hash_map.py`: Defines the hash map data structure used to store packages.

* `package.py`: Defines the `Package` class, representing a single package with attributes like ID, address, weight, and delivery status.

* `truck.py`: Defines the `Truck` class, which manages a truck's current location, loaded packages, and total mileage.

* `address_distance.py`: Contains the logic for calculating distances between addresses and determining the optimal delivery route.

* `CSV/`: This directory is intended to hold the CSV files that contain the package and address data.

## Setup and Installation

1.  Clone the repository:
    ```
    git clone [https://github.com/Rdmwebber/mail-delivery-service.git](https://github.com/Rdmwebber/mail-delivery-service.git)
    ```

2.  Navigate into the project directory:
    ```
    cd mail-delivery-service
    ```

3.  Ensure you have Python 3 installed.

4.  Place your address and package CSV files into the `CSV/` directory. The program expects specific formats for these files.

## Usage

To run the application, execute the `main.py` file from your terminal:
