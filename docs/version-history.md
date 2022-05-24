---
layout: page
title:	"California EPS Version History"
---
This page tracks updates that have been made with each version of the California Energy Policy Simulator.


### **3.3.1 - Jan. 18, 2022**

* New Features
  * Electricity Sector
    * Electricity generation subsidies can now be set separately for power plants of the same type in different quality tiers (both BAU and policy lever)
    * Electricity dispatch choice is now handled via a logit function rather than ALLOCATE AVAILABLE.  Logit shareweights are calculated endogenously and are policy-responsive.  A manual override for these shareweights has been added, allowing detailed customization of electricity dispatch behavior for regions with unusual electricity dispatch approaches.
  * Transportation Sector
    * Changes in the amount of money paid for passenger transport fares (airfare, bus fare, train fare) are now calculated.
    * Annual vehicle insurance costs for all on-road vehicles are now included.
    * Annual vehicle parking costs are now included.
    * Annual vehicle licensing, registration, and property tax costs are now included.
  * The fuel tax policy can now be used to reduce the BAU tax rate or apply subsidies.  Positive values increase the tax rate.  Negative values reduce the BAU tax rate or apply subsidies.
  * Added single-line graphs of total energy use for each end use sector.  Breakdowns showing total energy use as stacked area graphs already existed, but a single-line graph is sometimes preferable for simplicity or for comparing multiple policy packages on the same graph.

### **3.3.0 - Aug. 16, 2021**

* New Features
  * New Policy: Buy In-Region Products allows the user to specify a percentage of imported products (in the BAU case) that are shifted to domestic suppliers (in the policy case) for each individual industry.
  * Added demographic breakdowns disaggregating changes in lives saved due to reduced pollution by sex, race, and Hispanic or Latino status.  New graphs show results as absolute numbers and as percent changes relative to BAU.
  * The EPS core model structure now supports model run end dates as far out as 2100.  Each EPS region's developers may choose their preferred model run end date.  (The U.S. national model's end date remains 2050.)
  * New Policy: N<sub>2</sub>O abatement (from the chemicals industry, primarily from nitric and adipic acid production)
  * Projected future changes in BAU Output, BAU Employment, BAU Value Added, and BAU Employee Compensation disaggregated by ISIC code improve the accuracy of some input/output model results
* Web Interface
  * Added a new user interface (UI) for setting policy values and implementation schedules for multiple subscripted elements of the same policy.  Updates to WebAppData.xlsx format support the improved UI.

### **3.2.0 - Apr. 19, 2021**

* New Features
  * Added more detail to the Industry Category subscript, increasing the number of separately broken out industries from 8 to 25
  * Added new policy lever to enable mandated power plant retirement schedule 
  * Improved methodology for calculating the maximum amounts of power plant capacity and vehicles that can be deployed in a given year by implementing logit functions
  * Simplified input data requirements by removing energy suppliers from input variables and using internal calculations instead
  * Enabled new web app graph for carbon emissions by power plant type
  * Included new documentation, including guidance on all output graphs

### **3.1.2 - Feb. 18, 2021**

* New Features
  * Split ISIC 05T06 into coal mining (ISIC 05) and oil and gas extraction (ISIC 06)
* Data Updates
  * Updated emissions intensities for non-GHGs to align with EPA's National Emissions Inventory
  * Updated HFC data with values supplied by the U.S. Climate Alliance
  * BAU electricity subsidies updated for recent PTC and ITC extensions
  * Updated potential for industrial electrification, based on temperature ranges of industrial heat demand
  * Updated electric vehicle prices
  * Updated CCS costs
  * Other minor data input updates
 
### **3.0.0 - Oct 19, 2020**

* New Input-Output Model
  * An economic input/output (I/O) model has been added as a component of the Energy Policy Simulator.
  * New output metrics include the change in gross domestic product (GDP), employment (jobs), total employee compensation, average compensation per employee, number of union and non-union jobs, government spending, budget deficit/surplus, household tax revenue, payroll tax revenue, corporate income tax revenue, size of the national debt, and interest paid on the national debt.
  * Changes in GDP, jobs, and compensation can also be visualized disaggregated by economic sector or by their direct, indirect, and induced components.
  * Respending of changes in cash flow for government, households, and industries is now accounted for, providing a holistic look at policy impacts on economic activity.
  * New Government Revenue Accounting (GRA) settings allows the user to specify how government raises or spends changes in revenue caused by the policy package.  Options include changes in regular spending, deficit spending, household taxes, payroll taxes, and corporate income taxes.
  * Feedback loops from the I/O model to the Transportation, Buildings, and Industry sectors capture the energy demand and emissions associated with indirect and induced economic activity.
  * A new [documentation page](io-model.html) explains the I/O model in detail.
  * We gratefully acknowledge the invaluable contributions of the [American Council for an Energy-Efficient Economy](https://www.aceee.org/) (ACEEE), [Jim Barrett](https://www.barretteconomics.com/), and [Skip Laitner](https://www.linkedin.com/in/skip-laitner-746b124/) for their guidance and advice in implementing this feature, and for allowing us to learn from the [DEEPER I/O model](https://www.aceee.org/files/pdf/fact-sheet/DEEPER_Methodology.pdf), originally created by Skip Laitner.
* Improved Public Health Calculations
  * In addition to the policy package's effects on premature mortality (introduced in version 1.0.3), the EPS now calculates impacts on 10 additional health outcomes, including lost workdays, hospital admissions, non-fatal heart attacks, asthma attacks, respiratory symptoms and bronchitis.

### **2.1.1 - May 12, 2020**

* Major Improvements
  * Added capability to simulate COVID-19 recession impacts, adjustable in the web interface via a policy-like slider and implementation schedule.  This simulates effects of exogenous GDP changes on demand for energy, energy-using services, and products.  It can be adapted for different countries or reconfigured to represent other economic recessions (or booms) via updated input data.
  * The CCS policy lever has been overhauled.  It now is set in terms of a percentage of CO<sub>2</sub> captured, is subscripted by sector (electricity and industry sectors), and can be used to capture industrial process CO<sub>2</sub> and CO<sub>2</sub> from fuel burned to power the CCS process itself.

### **2.1.0 - Jan 21, 2020**

Note that starting with this release, Vensim 8 or later (64-bit) is required to run the Energy Policy Simulator. Update your copy of Vensim Model Reader for free from [Ventana Systems' website](https://vensim.com/free-download/).

* New Features
  * New Sector: Geoengineering.  Currently, the geoengineering sector includes one technology, direct air capture (DAC), and its associated policy.
  * Implemented cost-driven power plant retrofitting (such as coal-to-gas) and fuel type shifting (for instance, between crude oil, heavy fuel oil, and diesel)
  * New Policy: Subsidize electricity capacity construction

### **2.0.0 - Oct 7, 2019**

* New Hydrogen Supply Sector
  * There now exists a new sector in the EPS that calculates hydrogen production (in response to hydrogen demand from other sectors) and associated energy use, emissions, costs/savings, electricity demand response potential, etc.
  * New Policy: Shift Hydrogen Production Pathway (e.g. in the U.S., from steam reforming of natural gas to electrolysis)
  * District Heating Sector renamed District Heat and Hydrogen Sector, grouping these energy carriers in various totals and output graphs
* Fuels
  * Five new fuel types have been added: (1) crude oil, (2) heavy or residual fuel oil, (3) LPG / propane / butane, (4) municipal solid waste, and (5) hydrogen.  Each of these fuels has been added to each sector that can use it.
* Transportation Sector
  * Two new vehicle technologies have been added: LPG vehicle and hydrogen vehicle
  * New Policy: Reduce EV Range Anxiety and Charging Time (with support variable trans/BRAaCTSC)
  * New Policy: EV Charger Deployment (with support variable trans/EoCSoEVMS)
  * New Policy: Hydrogen Vehicle Sales Minimum
  * Removed EV Perks policy
  * Fuel economy standards are now subscripted by cargo type and vehicle type.  Applicable vehicle technologies are specified in a new input variable, trans/VTStFES.
  * Conventional pollutant standards for separately-regulated pollutants are now subscripted by pollutant type
* Industry Sector
  * New Policy: reduction in non-energy, non-agriculture industry product demand (e.g. material efficiency, product longevity, re-use, intensification of product use, etc.)
  * New Policy: reduction in fossil fuel exports
* Financial Calculations and Outputs
  * The Cash Flow Entity subscript has been redesigned.  It now contains the following nine entities: government, nonenergy industries, labor and consumers, foreign entities, electricity suppliers, coal suppliers, natural gas and petroleum suppliers, biomass and biofuel suppliers, other energy suppliers.  This helps with tracking cash flow allocations more uniformly and allows handling of imports and exports to/from the modeled region.

### **1.4.3 - January 15, 2020**
* Official launch of the California EPS