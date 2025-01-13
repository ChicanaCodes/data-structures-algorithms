# 🌟 Arrays: Introduction and Basic Operations 🌟

This example introduces arrays in Python using lists, covering how to:

1. 🧐 **Access Elements:** Learn how to retrieve specific elements using indices.  
2. ✍️ **Update Elements:** See how to modify elements in an array.  
3. 🔄 **Rotate Arrays:** Move elements in a circular manner where items wrap around the array.  
4. 🚚 **Shift Arrays:** Slide elements in one direction, padding the empty space with zeros.

---

## 🛠️ **What's in This Example?**

- 🎯 **Accessing Elements & Updating Elements:** Learn how to retrieve and modify elements using Python lists.  
   [📺 Watch the Video ▶️](https://youtube.com/shorts/7PubggmDrDU?si=mJEKPP9X5XAkj6aB)  

- 🔄 **Rotating & Shifting Arrays:** Learn how to rotate elements circularly and shift with zero padding.  
   [📺 Watch the Video ▶️](https://youtube.com/shorts/OPqNwut8go0?feature=share)  

---

## 📂 **File Contents**

- **[arrays_intro.py](arrays_intro.py)**: Demonstrates basic array access and update operations.  
- **[array_shifting_rotations.py](array_shifting_rotations.py)**: Covers both array shifting and rotation (left and right).  

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
2. **Run python code**
   ```bash
   python arrays_intro.py             # Access and update examples
   python array_shifting_rotations.py # Shifting and rotation examples

