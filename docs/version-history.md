---
layout: page
title:	"California EPS Version History"
---
This page tracks updates that have been made with each version of the California Energy Policy Simulator.


### **3.3.1 - June 16, 2022**

* New Input Data
  * Completely updated the input data and extended the time horizon from 2030 to 2050
  * New data uses a mix of CEC projections, E3 Pathways data, and other publicly available sources to project future energy demand and emissions.
  
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

* New Features
  * Added capability to simulate COVID-19 recession impacts, adjustable in the web interface via a policy-like slider and implementation schedule.  This simulates effects of exogenous GDP changes on demand for energy, energy-using services, and products.  It can be adapted for different countries or reconfigured to represent other economic recessions (or booms) via updated input data.
  * New Policy: Buy In-Region Products allows the user to specify a percentage of imported products (in the BAU case) that are shifted to domestic suppliers (in the policy case) for each individual industry.
  * Added demographic breakdowns disaggregating changes in lives saved due to reduced pollution by sex, race, and Hispanic or Latino status.  New graphs show results as absolute numbers and as percent changes relative to BAU.
  * The EPS core model structure now supports model run end dates as far out as 2100.  Each EPS region's developers may choose their preferred model run end date.  (The U.S. national model's end date remains 2050.)
  * New Policy: N<sub>2</sub>O abatement (from the chemicals industry, primarily from nitric and adipic acid production)
  * New policy lever to enable mandated power plant retirement schedule 
  * New Policy: Subsidize electricity capacity construction
  * New Policy: Shift Hydrogen Production Pathway (e.g. in the U.S., from steam reforming of natural gas to electrolysis)
  * New Policy: Reduce EV Range Anxiety and Charging Time (with support variable trans/BRAaCTSC)
  * New Policy: EV Charger Deployment (with support variable trans/EoCSoEVMS)
  * New Policy: Hydrogen Vehicle Sales Minimum
  * New Policy: reduction in non-energy, non-agriculture industry product demand (e.g. material efficiency, product longevity, re-use, intensification of product use, etc.)
  * New Policy: reduction in fossil fuel exports
  * New Policy: shift animal product use to non-animal product use
  * New Policy: Fuel Price Deregulation
  * A new control lever, plcy-ctrl-ctr/BENCEfCT, allows non-CO2 emissions to be exempted from the carbon tax
  * New Policy: Toggle Whether Carbon Tax Affects Process Emissions (reverses the behavior of the corresponding control lever in the policy case)
  * New Policy: Toggle Whether Carbon Tax Affects Non CO2 Emissions (reverses the behavior of the corresponding control lever in the policy case)
  * A new control lever, plcy-ctrl-ctr/BAEPAbCiGC, controls whether policy-driven changes in electricity generators' costs affect electricity prices
  * Projected future changes in BAU Output, BAU Employment, BAU Value Added, and BAU Employee Compensation disaggregated by ISIC code improve the accuracy of some input/output model results
  * Added more detail to the Industry Category subscript, increasing the number of separately broken out industries from 8 to 25

* New Sectors
  * Geoengineering.  Currently, the geoengineering sector includes one technology, direct air capture (DAC), and its associated policy.
  * New Hydrogen Supply Sector
	* There now exists a new sector in the EPS that calculates hydrogen production (in response to hydrogen demand from other sectors) and associated energy use, emissions, costs/savings, electricity demand response potential, etc.
	* New Policy: Shift Hydrogen Production Pathway (e.g. in the U.S., from steam reforming of natural gas to electrolysis)
	* District Heating Sector renamed District Heat and Hydrogen Sector, grouping these energy carriers in various totals and output graphs

* Fuels
  * Five new fuel types have been added: (1) crude oil, (2) heavy or residual fuel oil, (3) LPG / propane / butane, (4) municipal solid waste, and (5) hydrogen.  Each of these fuels has been added to each sector that can use it.

* Financial Calculations and Outputs
  * The Cash Flow Entity subscript has been redesigned.  It now contains the following nine entities: government, nonenergy industries, labor and consumers, foreign entities, electricity suppliers, coal suppliers, natural gas and petroleum suppliers, biomass and biofuel suppliers, other energy suppliers.  This helps with tracking cash flow allocations more uniformly and allows handling of imports and exports to/from the modeled region.

* Web Interface
  * Added a new user interface (UI) for setting policy values and implementation schedules for multiple subscripted elements of the same policy.  Updates to WebAppData.xlsx format support the improved UI.
  
### **1.4.3 - January 15, 2020**
* Official launch of the California EPS