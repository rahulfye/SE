# Lab 3: Component Modelling & Architectural Pattern Selection

**Course:** Software Engineering Labs (SELABS)  
**Assigned System:** Self-Service Coffee Kiosk System  
**Deliverables Directory:** `/Users/rahuldutta/Downloads/Lab 3`

---

## 1. Executive Summary & Required Deliverables Checklist

Per the lab manual instructions, here are the required deliverables completed and available in this folder:

| Required Deliverable | Lab Manual Requirement | File Name in Workspace | Description |
|---|---|---|---|
| **Component Diagram (PNG)** | At least 5 components, 4 interfaces, UML ball & socket notation | `Coffee_Kiosk_Component_Diagram.png` | High-resolution UML 2.0 component diagram |
| **Component Diagram (PDF)** | Vector / export format of the diagram | `Coffee_Kiosk_Component_Diagram.pdf` | Print-ready PDF export of the component diagram |
| **Component Diagram (Draw.io)** | draw.io format recommended in Step 4 | `Coffee_Kiosk_Component_Diagram.drawio` | Editable XML file for [draw.io / diagrams.net](https://app.diagrams.net) |
| **Component Diagram (Source)** | PlantUML source code | `Coffee_Kiosk_Component_Diagram.puml` | Re-compilable PlantUML source code |
| **Written Justification (DOCX)** | Word document (max 1 page) with required structure | `Coffee_Kiosk_Architecture_Justification.docx` | Formatted Word document per lab manual specifications |
| **Written Justification (PDF)** | PDF version of the 1-page justification | `Coffee_Kiosk_Architecture_Justification.pdf` | Exactly 1-page PDF document ready for submission |
| **Comprehensive Lab Report** | Step-by-step documentation (Steps 1–6) | `Lab_3_Comprehensive_Report.md` / `README.md` | Full academic documentation for Git submission |

---

## 2. Step 1: Scenario Review & Requirements Analysis

### 2.1 Scenario Description
You are designing the software architecture for a **Self-Service Coffee Kiosk system** in a busy café. The kiosk must provide an automated, reliable ordering experience on dedicated kiosk hardware.

### 2.2 Functional Requirements (FR)
- **FR-1 (Beverage Selection):** Customers can select from three coffee types: **Espresso**, **Americano**, and **Latte**.
- **FR-2 (Drink Sizing):** Customers can choose between two drink sizes: **Small** and **Large**.
- **FR-3 (Payment Processing):** System accepts payments via **Credit Card only** (no cash or debit pins).
- **FR-4 (Receipt Generation):** System prints physical receipts detailing itemized orders, sizing, total price, and transaction metadata.

### 2.3 Technical & Hardware Constraints
- **TC-1 (Touchscreen Input):** Software must handle responsive touch-screen interactions and UI updates.
- **TC-2 (Receipt Hardware):** Must interface directly with physical thermal printer hardware (ESC/POS serial/USB).
- **TC-3 (Menu & Pricing Storage):** Must store, look up, and persist menu catalog data, pricing matrices, and sales transaction logs.

### 2.4 Key Non-Functional Challenges
- **Usability:** Fast, intuitive touchscreen UI suitable for all customer demographics in a high-throughput queue.
- **Performance:** Low-latency touch responsiveness (< 100 ms) and immediate order dispatch to avoid café queues.
- **Security:** Strict cardholder data protection (PCI-DSS compliance), preventing unauthorized access to financial tokens or raw pricing tables via kiosk UI tampering.
- **Reliability:** Operational stability on a standalone kiosk terminal, functioning seamlessly without relying on high-latency remote cloud round-trips for local order selection.

---

## 3. Step 2: Architectural Style Analysis

| Architectural Style | Key Structural Characteristics | Pros | Cons | Suitability for Coffee Kiosk |
|---|---|---|---|---|
| **Layered Architecture (Selected)** | Horizontal tiers (Presentation, Business, Data). Components communicate only through adjacent layers. | • Strict separation of concerns<br>• Zero network latency on local kiosk<br>• Straightforward deployment & maintenance<br>• Isolates hardware drivers | • Not suited for massively distributed micro-scaling | **HIGH (Optimal):** Ideal for dedicated single-terminal embedded/POS kiosk hardware. |
| **Microservices Architecture** | Small, autonomous services communicating over HTTP/gRPC networks. | • Independent deployment<br>• Polyglot technology stacks<br>• Scalable per service | • High operational complexity<br>• Network latency on basic UI actions<br>• Hardware drivers difficult to split across nodes | **LOW:** Major overkill for a single café kiosk; introduces network failure points. |
| **Client-Server Architecture** | Centralized backend server accessed by dumb client terminals. | • Centralized menu & price management<br>• Simple client thin logic | • Single point of failure<br>• Network outage locks out kiosk terminal entirely | **MEDIUM:** Useful for multi-store chains, but kiosk must still operate standalone if café Wi-Fi fluctuates. |

---

## 4. Step 3: Architecture Selection & Component Identification

### 4.1 Architecture Selection
**"We chose Layered Architecture for the Self-Service Coffee Kiosk System."**

### 4.2 Component Identification (5 Components)
1. **User Interface Component (Presentation Layer):**
   - Renders the graphical user interface on the kiosk touchscreen display.
   - Captures user touch events for coffee type (Espresso, Americano, Latte) and size (Small, Large).
   - Prompts for payment and displays order progress.
   - *Interface:* Requires `Order Interface`.

2. **Order Manager Component (Business Layer - Core):**
   - Coordinates the end-to-end ordering workflow.
   - Calculates total price based on coffee type, size, and applicable taxes.
   - Dispatches payment authorization requests and commands receipt generation upon approval.
   - *Interface:* Provides `Order Interface`; Requires `Payment Interface`, `Receipt Interface`, and `Database Interface`.

3. **Payment Service Component (Business Layer - Financial Integration):**
   - Handles credit card processing requests exclusively.
   - Interfaces securely with the attached physical card terminal / payment chip reader.
   - Encapsulates payment tokens, transaction authorization, and PCI-DSS compliance.
   - *Interface:* Provides `Payment Interface`.

4. **Receipt Printer Component (Business Layer - Hardware Controller):**
   - Connects directly to the thermal receipt printer hardware.
   - Formats the order summary (item names, sizes, price, transaction ID, date/time) into ESC/POS commands.
   - Monitors printer status (paper low, printer online/offline).
   - *Interface:* Provides `Receipt Interface`.

5. **Database Component (Data Layer - Persistence):**
   - Manages local persistence for menu items, pricing matrices, and sales transaction logs.
   - Provides read/write access via structured SQL/ORM queries.
   - *Interface:* Provides `Database Interface`.

---

## 5. Step 4: UML Component Diagram & Interface Specifications

### 5.1 Diagram Structure
```
+-----------------------------------------------------------------------------------+
|                              PRESENTATION LAYER                                   |
|   +---------------------------------------------------------------------------+   |
|   |                        User Interface Component                           |   |
|   +---------------------------------------------------------------------------+   |
+-----------------------------------------|-(---------------------------------------+
                                          |   Order Interface (API)
+-----------------------------------------O-----------------------------------------+
|                                BUSINESS LAYER                                     |
|   +---------------------+   +---------------------+   +-----------------------+   |
|   |   Receipt Printer   |   |    Order Manager    |   |    Payment Service    |   |
|   |      Component      |   |      Component      |   |       Component       |   |
|   +----------O----------+   +----------|-(--------+   +-----------O-----------+   |
|              |                         |                          |               |
|              +-----------)-)-----------+------------)-(-----------+               |
|            Receipt Interface                      Payment Interface               |
+-----------------------------------------|-(---------------------------------------+
                                          |   Database Interface (SQL Queries)
+-----------------------------------------O-----------------------------------------+
|                                  DATA LAYER                                       |
|   +---------------------------------------------------------------------------+   |
|   |                            Database Component                             |   |
|   +---------------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------------+
```

### 5.2 Key Interfaces (Ball & Socket Notation)

1. **Order Interface (`IOrderService`):**
   - **Provider (Ball):** `Order Manager Component`
   - **Consumer (Socket):** `User Interface Component`
   - **Type / Protocol:** In-process event API / Direct method calls
   - **Methods / Data:** `getMenu()`, `selectDrink(type, size)`, `submitOrder()`, `getOrderStatus()`

2. **Payment Interface (`IPaymentService`):**
   - **Provider (Ball):** `Payment Service Component`
   - **Consumer (Socket):** `Order Manager Component`
   - **Type / Protocol:** Secure API / Encrypted Payment Token Bus (PCI-DSS)
   - **Methods / Data:** `authorizePayment(amount, currency)`, `captureTransaction(authId)`, `getTransactionResult()`

3. **Receipt Interface (`IPrinterService`):**
   - **Provider (Ball):** `Receipt Printer Component`
   - **Consumer (Socket):** `Order Manager Component`
   - **Type / Protocol:** Hardware Device Driver / ESC/POS Protocol (USB/Serial)
   - **Methods / Data:** `printReceipt(orderSummary, receiptDetails)`, `checkPrinterStatus()`

4. **Database Interface (`IDataAccessService`):**
   - **Provider (Ball):** `Database Component`
   - **Consumer (Socket):** `Order Manager Component`
   - **Type / Protocol:** Structured SQL Queries / Local ORM
   - **Methods / Data:** `fetchMenuCatalog()`, `fetchPricing(drinkType, size)`, `saveCompletedOrder(orderRecord)`

---

## 6. Step 5: Written Justification (Submission Text)

Below is the exact text generated in `Coffee_Kiosk_Architecture_Justification.docx` and `Coffee_Kiosk_Architecture_Justification.pdf`:

> **Architecture Selection:**  
> *"We chose Layered Architecture for the Self-Service Coffee Kiosk System."*
> 
> **1. Architectural Choice:**  
> A 3-Tier Layered Architecture comprising the **Presentation Layer** (User Interface Component), **Business Layer** (Order Manager Component, Payment Service Component, Receipt Printer Component), and **Data Layer** (Database Component). This design decomposes the kiosk into discrete, loosely-coupled horizontal layers interacting strictly through formal provided/required interfaces.
> 
> **2. Scenario-Related Reasons for Selection:**  
> - **Reason 1 — Hardware Peripheral Decoupling & Modularity:** The kiosk relies on dedicated hardware components: a touchscreen display, a credit card payment terminal, and a thermal receipt printer. Layering isolates hardware drivers and protocols (ESC/POS commands, payment terminal APIs) inside dedicated business/service components. This ensures that changing receipt printer hardware or updating the touch UI layout has zero ripple effect on core order pricing or business rules.  
> - **Reason 2 — Operational Simplicity & High Availability:** The kiosk functions as a standalone, high-traffic ordering terminal in a busy café offering a focused menu (Espresso, Americano, Latte in Small/Large sizes). Unlike a Microservices architecture which introduces distributed network latency, container orchestration, and multi-service failure modes, or a Client-Server setup vulnerable to total terminal lockout during network outages, Layered Architecture provides a robust, self-contained deployment.
> 
> **3. Security Advantage:**  
> **Cardholder Data Isolation & Defense-in-Depth:** Transactions are restricted to credit cards only. In our layered architecture, the Presentation Layer possesses zero direct connectivity to the database or external payment networks. Sensitive payment authorization is encapsulated exclusively inside the Payment Service Component conforming to PCI-DSS standards. Customers cannot trigger unauthorized SQL queries or tamper with pricing data via the touchscreen interface, ensuring end-to-end security.
> 
> **4. Performance Benefit:**  
> **Zero-Network Latency & Instant Touch Responsiveness:** In a busy café, rapid queue turnover is vital. Because layers communicate via in-process method calls on the local terminal rather than network RPC/REST calls, UI actions (beverage selection, size toggling, order reviews) execute with sub-millisecond responsiveness. Menu catalog and pricing queries are served directly from the local Database Component, eliminating network latency bottlenecks and UI stalls.

---

## 7. Submission Checklist for GitHub Repo (`SELABS/Lab3`)

To submit your lab work:
1. Copy or push the following files into your Git repository folder (e.g. `Lab3/` under your `SELABS` repository):
   - `Coffee_Kiosk_Component_Diagram.png` *(Component Diagram Image)*
   - `Coffee_Kiosk_Component_Diagram.pdf` *(Component Diagram PDF)*
   - `Coffee_Kiosk_Component_Diagram.drawio` *(Editable Draw.io XML)*
   - `Coffee_Kiosk_Component_Diagram.puml` *(PlantUML source)*
   - `Coffee_Kiosk_Architecture_Justification.docx` *(Word Document Justification)*
   - `Coffee_Kiosk_Architecture_Justification.pdf` *(1-Page PDF Justification)*
   - `README.md` *(This documentation)*
2. Commit and push:
   ```bash
   git add .
   git commit -m "Submit Lab 3: Component Modelling & Architectural Pattern Selection"
   git push origin main
   ```
