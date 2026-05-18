# 🎫 Advanced Railway Reservation & Operational Management System

An elegant, high-performance desktop application migrating legacy railway processing architectures into a modernized, fluid Python 3 ecosystem driven by **PyQt6**. Built with structural UI/UX paradigms, a dynamic station fare engine, active calendar syncing, and live session verification tracking.

---

## 🔐 Default Administrative Credentials

The system entryway is protected by a local credential verification shield. Use the authorized credentials below to clear the portal:

| Role | Authorized Username | System Access Password |
| :--- | :--- | :--- |
| **System Administrator** | `Pranav0004` | `Bobby0004` |

---

## 🔄 System Flow Matrix

```text
Admin inputs credentials -> Verifies against secure memory block
      ↓
Gateway authentication success -> Prompts MainWindow desktop workspace
      ↓
Admin selects "Book Ticket" tab -> Inputs Passenger details & Route parameters
      ↓
Live engine computes sector price matrix -> Displays calculated fare instantly
      ↓
Admin clicks "Confirm Booking" -> Commits record to memory ledger & spawns confirmation window
      ↓
System updates History Ledger -> Dynamic view refreshes with new record tracking indices

---

# 🛠️ Built With

* **Language Platform:** Python 3.10+
* **Core Graphical Engine:** PyQt6 (Qt v6 Desktop Development Kit)
* **Design Pattern:** Component-based UI Stack Architecture

---

# 🛠️ Built With

| Platform Element | System Specification |
| :--- | :--- |
| **Language Platform** | Python 3.10+ |
| **Core Graphical Engine** | PyQt6 (Qt v6 Desktop Development Kit) |
| **Design Pattern** | Component-based UI Stack Architecture |

---

# 📊 Core Runtime Data Models

Since the application runs a lightweight, ultra-fast structural operational design, data records are tracked via active memory structures mimicking schema arrays.

### 1. Account Identity Array (`login.py`)

| Variable Attribute | Virtual Field Type | Description / Constraints |
| :--- | :--- | :--- |
| `username` | `VARCHAR` | Unique access identification identifier (`Pranav0004`) |
| `password` | `VARCHAR` | Case-sensitive secure gateway verification pass (`Bobby0004`) |

### 2. Journey Transaction Array (`journey.py`)

| Variable Attribute | Virtual Field Type | Description / Constraints |
| :--- | :--- | :--- |
| `passenger_name` | `VARCHAR` | Clear-text traveler metadata string |
| `source_from` | `VARCHAR` | Origin station boundary picked from combobox indexing |
| `destination_target` | `VARCHAR` | Terminal arrival target station |
| `journey_date` | `DATE` | Calendar widget selection timestamp value |
| `fare_cleared` | `DECIMAL` | Evaluated sector pricing finalized by calculation engine |
