# 🌟 Arrays and Strings: Introduction and Basic Operations 🌟

This repository introduces fundamental concepts in Python, starting with arrays and strings. Learn how to work with these essential data structures and prepare for technical coding interviews.

---

## 🌟 **Topics Covered**

### Arrays
1. 🧐 **Access Elements:** Learn how to retrieve specific elements using indices.  
2. ✍️ **Update Elements:** See how to modify elements in an array.  
3. 🔄 **Rotate Arrays:** Move elements in a circular manner where items wrap around the array.  
4. 🚚 **Shift Arrays:** Slide elements in one direction, padding the empty space with zeros.  

### Strings
1. 📜 **Define Strings:** Understand how to create and work with text in Python.  
2. 🔄 **Reverse Strings:** Learn to reverse text using slicing.  
3. 🪞 **Palindrome Check:** Check if a word reads the same forward and backward.  
4. 🔗 **Joining and Splitting Strings:** Combine or break apart strings with Python’s built-in methods.

---

## 🛠️ **What's in This Example?**

### Arrays
- 🎯 **Accessing Elements & Updating Elements:** Learn how to retrieve and modify elements using Python lists.  
   [📺 Watch the Video ▶️](https://youtube.com/shorts/7PubggmDrDU?si=7OH0DNKp-fi8so6z)  

- 🔄 **Rotating & Shifting Arrays:** Learn how to rotate elements circularly and shift with zero padding.  
   [📺 Watch the Video ▶️](https://youtube.com/shorts/OPqNwut8go0?feature=share)  

### Strings
- 📜 **Strings Introduction:** Learn how to define, reverse, and manipulate strings.  
   [📺 Watch the Video ▶️](https://youtube.com/shorts/7WWnvNtH-BE?feature=share)  

---

## 📂 **File Contents**

- **[arrays_intro.py](arrays_intro.py)**: Demonstrates basic array access and update operations.  
- **[array_shifting_rotations.py](array_shifting_rotations.py)**: Covers both array shifting and rotation (left and right).  
- **[strings_intro.py](strings_intro.py)**: Introduces strings with examples on reversing, palindromes, and joining strings.

---

## 💡 **Key Differences Between Rotation and Shifting:**

| Feature                        | 🔄 **Rotation**                | 🚚 **Shifting**               |
|:-------------------------------|:------------------------------:|:-----------------------------:|
| **Movement Type**              | Circular 🔁                   | Linear (One-way) ➡️           |
| **Data Loss?**                 | No data loss ✅               | Elements removed ❌            |
| **Size Change?**               | Remains the same ✅            | Zeroes added to maintain size ⭕ |
| **Example (Shift Right by 2)** | `[1,2,3,4,5] → [4,5,1,2,3]` | `[1,2,3,4,5] → [0,0,1,2,3]`    |
| **Use Cases**                  | Circular buffers, cyclic data | Data cleaning, padding gaps   |

---

## 💻 **Running the Code**

1. **Clone this repository:**
   ```bash
   git clone https://github.com/ChicanaCodes/data-structures-algorithms.git
   cd arraysStrings

## 💻 **Running the Code**

1. **Clone this repository:**
   ```bash
   git clone https://github.com/ChicanaCodes/data-structures-algorithms.git
   cd arraysStrings
2. **Run python code**
   ```bash
   python arrays_intro.py             # Access and update examples
   python array_shifting_rotations.py # Shifting and rotation examples
   python strings_intro.py

