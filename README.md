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
🛠️ Built WithLanguage Platform: Python 3.10+Core Graphical Engine: PyQt6 (Qt v6 Desktop Development Kit)Design Pattern: Component-based UI Stack Architecture📊 Core Runtime Data ModelsSince the application runs a lightweight, ultra-fast structural operational design, data records are tracked via active memory structures mimicking schema arrays.1. Account Identity Array (login.py)Variable AttributeVirtual Field TypeDescription / ConstraintsusernameVARCHARUnique access identification identifier (Pranav0004)passwordVARCHARCase-sensitive secure gateway verification pass (Bobby0004)2. Journey Transaction Array (journey.py)Variable AttributeVirtual Field TypeDescription / Constraintspassenger_nameVARCHARClear-text traveler metadata stringsource_fromVARCHAROrigin station boundary picked from combobox indexingdestination_targetVARCHARTerminal arrival target stationjourney_dateDATE (yyyy-MM-dd)Calendar widget selection timestamp valuefare_clearedDECIMAL / CURRENCYEvaluated sector pricing finalized by calculation engine⚙️ Installation & Setup InstructionsFollow these structured development environment initialization parameters to spin up the local system workspace.1. Verify PrerequisitesEnsure your operating terminal has Python 3.10 or higher installed alongside the pip dependency manager.Bashpython --version
pip --version
2. Environment Dependencies SetupInstall the necessary graphical bindings to compile the application widgets cleanly:Bashpip install PyQt6
3. Move Into Your Work DirectoryJump into the local directory containing the source execution scripts:Bashd:
cd \railway-python-dashboard
4. Run the Core System ThreadExecute the master controller file to build the system layout windows:Bashpython main.py
📁 Repository Workspace BlueprintPlaintextrailway-reservation-system/
│
├── main.py          # Master application driver, layout manager, and global timer thread
├── login.py         # Administrative credential scanner and gatekeeper widget layout
└── journey.py       # Core transaction engine, pricing matrices, and dynamic history data frames
👤 Structural Engineering GroupLead Project Architect: PRANAV M
