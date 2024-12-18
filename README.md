# Music Store Management System

## Objective
The Music Store Management System is designed to manage musical instruments and operations within a music store. This project supports various functionalities, including inventory management, instrument sorting, sales, handling, and audio simulations, to provide an interactive and efficient user experience.

---

## Features

1. **Add New Instrument**:
   - Allows the user to add new musical instruments to the system.
   - Categorized by type (e.g., stringed, percussion, wind, keyboard).

2. **View Store Data**:
   - Displays store information, including the total number of instruments, cash flow, and sales data.

3. **Sort Instruments**:
   - Sort inventory based on price or year (ascending/descending).

4. **Instrument Operations**:
   - Sell instruments based on catalog numbers.
   - View detailed information and location of a specific instrument in the inventory.
   - Play a simulation sound for an instrument.

5. **Discounts and Price Updates**:
   - Apply percentage-based discounts to all instruments.
   - Update the price of specific instruments.

6. **Guitar Handling**:
   - Support for setup, string replacement, and repair operations.

7. **Jam Sessions**:
   - Simulate a jam session with available instruments.

8. **Save Store Data**:
   - Save current store data to a text file for record-keeping.

9. **Exit**:
   - Exit the system with a friendly farewell message.

---

## Class Structure

### Core Classes
- **`Instrument`**: Base class for all instruments.
  - Attributes: brand, model, color, weight, year, price, catalog number.
  - Methods: `__repr__`, `__str__`, `GetInstrument()`.

### Derived Classes
- **`Stringed`**: Adds number of strings.
- **`Bow`**: Adds size attributes (e.g., for violins, cellos).
- **`Guitar`**: Adds wood type.
  - Subclasses: `Bass`, `Accoustic`, `Classic`, `Electric`.
- **`Wind`**: Adds material type.
  - Subclasses: `Trumpet`, `Saxophone`, `Flute`.
- **`Keyboard`**: Adds number of keys.
  - Subclasses: `Organ`, `Piano`.
- **`Percussion`**: Adds stick count.
  - Subclasses: `Drums`.

### Handling Classes
- **`Handling`**: Base class for maintenance operations.
  - Subclasses: `Setup`, `ChangeStrings`, `Repair`.

### Container Class
- **`MusicStore`**: Manages store operations and inventory.
  - Attributes: name, list of instruments, cash flow, sales count.
  - Methods: sorting, selling, saving data, handling operations, etc.

---

## File Overview

### Source Code
- **`project.2.0.py`**: Contains all class definitions and the main menu system.

### Output Data
- **`output.txt`**: Example store data saved by the system:
  ```
  The business name is: Music-Center
  Amount of instruments:
  There are 1 instruments in the store.
  The cash-flow of the store is:  5328.0 shekel.
  Instrument list:
  *****************************************:
  Bass Guitar:
  Instrument's data :
  Brand :  asd
  Model :  asd
  Color :  asd
  Weight :  2.0 KG
  Year :  2020
  Price :  1234.0 shekel
  Catalog number :  1234
  Number of strings :  4
  The wood type is :  ash
  The neck wood type is :  maple
  *****************************************:
  ```

---

## Prerequisites
- Python 3.x
- Required modules: `winsound`

---

## Usage
1. Run the `project.2.0.py` script.
2. Follow the interactive menu to perform operations.
3. Save store data to a file for later use.

---

## Future Enhancements
1. **User Interface**: Develop a graphical user interface (GUI) for better usability.
2. **Database Integration**: Use a database for persistent storage instead of text files.
3. **Enhanced Sound Effects**: Include more realistic sound simulations.
4. **Analytics**: Add analytics for sales trends and popular instruments.

---

## Acknowledgments
- Developed as a final project to demonstrate object-oriented programming and system design skills.
