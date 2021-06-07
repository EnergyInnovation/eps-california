# CreateContributionTestScript.py
#
# Developed by Jeffrey Rissman
#
# This is a Python script that is used to generate a Vensim command script.
# The Vensim command script will perform one run with all selected policies
# enabled, one run with all policies disabled (a BAU run),
# and one run with each defined subset (or "group") within the set of selected
# policies turned off or turned on (depending on a user setting in this script).


# File Names
# ----------
# Rather than including input and output file names in the code below, we assign all the file
# names to variables in this section.  This allows the names to be easily changed if desired.
ModelFile = "EPS.mdl" # The name of the Vensim model file (typically with .mdl or .vpmx extension)
FirstYear = "2019" # The first year you wish to include in the output file (cannot be prior to first simulated year)
FinalYear = "2050" # The last year you wish to include in the output file (cannot be later than last simulated year)
OutputScript = "GeneratedContributionTestScript.cmd" # The desired filename of the Vensim command script to be generated
RunResultsFile = "ContributionTestResults.tsv" # The desired filename for TSV file containing model run results
OutputVarsFile = "OutputVarsForWedgeDiagram.lst" # The name of the file containing a list of variables to be included in the RunResultsFile
                                                 # May optionally also be used as a SAVELIST for Vensim (see below)

# Other Settings
# --------------
RunName = "MostRecentRun" # The desired name for all runs performed.  Used as the filename for the .vdfx files that Vensim creates
EnableOrDisableGroups = "Disable" # Should each group be enabled or disabled in turn?
								 # Essentially, this is testing either the contribution of a group in the proximity of the
								 # BAU case ("Enable") or in the proximity of a scenario defined in the non-zero values of
								 # the policies listed below ("Disable").
PolicySchedule = 3 # The number of the policy implementation schedule file to be used (in InputData/plcy-schd/FoPITY)


# Index definitions
# -----------------
# Each policy is a Python list.  The numbers below are a key to the meaning of the four entries
# that compose each policy, so we can refer to them by meaningful names in the code.
# Note that the fourth entry in each policy, Settings, is itself a list that contains various
# setting values.  Do not change any names or numbers in this section.
Enabled = 0
LongName = 1
ShortName = 2
Settings = 3
Group = 4


# Policy Options
# --------------
# This section specifies which policies should be included in the Vensim command script
# (called here "enabled" policies) and what setting values for those policies should
# be included.  Unless you are using "Enable" Groups mode, all non-repeating
# combinations of the settings for enabled policies will
# be included in the Vensim command script, so do not enable too many policies at once, or
# Vensim will be unable to complete the necessary runs in a reasonable amount of time.
# Each policy is on a single line:
  # You may change the first entry of each policy to "True" to enable the policy or "False" to disable it.
  # The second and third entries are the long and short name of the policy, used internally by this script.  Do not change these names.
  # The fourth entry in each policy is a list of setting values enclosed with square brackets.
    # You may change these values, add more values (separated by commas), and delete values.
    # Any enabled policy must have a minimum of one setting value.  A policy that is disabled
    # and a policy with a setting of zero produce identical results.
  # The fifth entry in each policy is its group name.  By default, each policy is in its own group (and its subscripts share that group).
    # Change the group names so multiple policies share a name (like "financial policies") to cause them to be enabled or disabled together.

PotentialPolicies = (

    (True, "Additional Minimum Required EV Sales Percentage[passenger,LDVs]","Additional Minimum Required EV Sales Percentage[passenger,LDVs]",[0,1],"Passenger Car ZEV Sales Standard"),
    (True, "Additional Minimum Required EV Sales Percentage[passenger,HDVs]","Additional Minimum Required EV Sales Percentage[passenger,HDVs]",[0,1],"California HDV Rules"),
    (True, "Additional Minimum Required EV Sales Percentage[passenger,motorbikes]","Additional Minimum Required EV Sales Percentage[passenger,motorbikes]",[0,1],"California HDV Rules"),
    (True, "Additional Minimum Required EV Sales Percentage[freight,LDVs]","Additional Minimum Required EV Sales Percentage[freight,LDVs]",[0,1],"California HDV Rules"),
    (True, "Additional Minimum Required EV Sales Percentage[freight,HDVs]","Additional Minimum Required EV Sales Percentage[freight,HDVs]",[0,1],"California HDV Rules"),
    (True, "Annual Additional Capacity Retired due to Early Retirement Policy[hard coal es]","Annual Additional Capacity Retired due to Early Retirement Policy[hard coal es]",[0,292.06],"Power Sector Coal Regs"),
    (True, "Boolean Ban New Power Plants[hard coal es]","Boolean Ban New Power Plants[hard coal es]",[0,1],"Power Sector Coal Regs"),
    (True, "Boolean Ban New Power Plants[natural gas nonpeaker es]","Boolean Ban New Power Plants[natural gas nonpeaker es]",[0,1],"Power Sector Gas Regs"),
    (True, "Boolean Ban New Power Plants[lignite es]","Boolean Ban New Power Plants[lignite es]",[0,1],"Power Sector Coal Regs"),
    (True, "Electricity Sector Fraction of Potential Additional CCS Achieved[petroleum es]","Electricity Sector Fraction of Potential Additional CCS Achieved[petroleum es]",[0,1],"Power Sector Gas Regs"),
    (True, "Electricity Sector Fraction of Potential Additional CCS Achieved[natural gas peaker es]","Electricity Sector Fraction of Potential Additional CCS Achieved[natural gas peaker es]",[0,1],"Power Sector Gas Regs"),
    (True, "Fraction of Additional Demand Response Potential Achieved","Fraction of Additional Demand Response Potential Achieved",[0,1],"Grid Flexibility"),
    (True, "Fraction of Additional Grid Battery Storage Potential Achieved","Fraction of Additional Grid Battery Storage Potential Achieved",[0,1],"Grid Flexibility"),
    (True, "Fraction of Afforestation and Reforestation Achieved","Fraction of Afforestation and Reforestation Achieved",[0,1],"Afforestation and Reforestation"),
    (True, "Fraction of Cement Measures Achieved","Fraction of Cement Measures Achieved",[0,1],"Cement Clinker Substitution"),
    (True, "Fraction of Cropland and Rice Measures Achieved","Fraction of Cropland and Rice Measures Achieved",[0,1],"Cropland Measures"),
    (True, "Fraction of F Gas Destruction Achieved","Fraction of F Gas Destruction Achieved",[0,0.7251],"F-Gas Policies"),
    (True, "Fraction of F Gas Substitution Achieved","Fraction of F Gas Substitution Achieved",[0,1],"F-Gas Policies"),
    (True, "Fraction of Hydrogen Production Pathways Shifted","Fraction of Hydrogen Production Pathways Shifted",[0,1],"Hydrogen Electrolysis"),
    (True, "Fraction of Improved Forest Management Achieved","Fraction of Improved Forest Management Achieved",[0,1],"Forest Management"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,hard coal if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,hard coal if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,natural gas if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,natural gas if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,petroleum diesel if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,petroleum diesel if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,heavy or residual fuel oil if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,heavy or residual fuel oil if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,LPG propane or butane if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,LPG propane or butane if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,hard coal if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,hard coal if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,natural gas if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,natural gas if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,biomass if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,biomass if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,crude oil if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,crude oil if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,hard coal if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,hard coal if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,natural gas if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,natural gas if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,petroleum diesel if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,petroleum diesel if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,heavy or residual fuel oil if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,heavy or residual fuel oil if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,LPG propane or butane if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,LPG propane or butane if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,hard coal if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,hard coal if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,natural gas if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,natural gas if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,petroleum diesel if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,petroleum diesel if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,heavy or residual fuel oil if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,heavy or residual fuel oil if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,LPG propane or butane if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,LPG propane or butane if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,hard coal if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,hard coal if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,natural gas if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,natural gas if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,petroleum diesel if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,petroleum diesel if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,heavy or residual fuel oil if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,heavy or residual fuel oil if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,natural gas if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,natural gas if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,petroleum diesel if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,petroleum diesel if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,heavy or residual fuel oil if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,heavy or residual fuel oil if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,LPG propane or butane if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,LPG propane or butane if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,hard coal if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,hard coal if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,natural gas if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,natural gas if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,petroleum diesel if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,petroleum diesel if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,heavy or residual fuel oil if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,heavy or residual fuel oil if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,LPG propane or butane if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,LPG propane or butane if]",[0,1],"Industrial Electrification and Hydrogen"),
    (True, "Fraction of Livestock Measures Achieved","Fraction of Livestock Measures Achieved",[0,1],"Livestock Measures"),
    (True, "Fraction of Methane Capture Opportunities Achieved[natural gas and petroleum systems]","Fraction of Methane Capture Opportunities Achieved[natural gas and petroleum systems]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Capture Opportunities Achieved[coal mining]","Fraction of Methane Capture Opportunities Achieved[coal mining]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Capture Opportunities Achieved[waste management]","Fraction of Methane Capture Opportunities Achieved[waste management]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Destruction Opportunities Achieved[natural gas and petroleum systems]","Fraction of Methane Destruction Opportunities Achieved[natural gas and petroleum systems]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Destruction Opportunities Achieved[coal mining]","Fraction of Methane Destruction Opportunities Achieved[coal mining]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Destruction Opportunities Achieved[waste management]","Fraction of Methane Destruction Opportunities Achieved[waste management]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[heating,urban residential]","Fraction of New Bldg Components Shifted to Other Fuels[heating,urban residential]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[heating,rural residential]","Fraction of New Bldg Components Shifted to Other Fuels[heating,rural residential]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[heating,commercial]","Fraction of New Bldg Components Shifted to Other Fuels[heating,commercial]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[appliances,urban residential]","Fraction of New Bldg Components Shifted to Other Fuels[appliances,urban residential]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[appliances,rural residential]","Fraction of New Bldg Components Shifted to Other Fuels[appliances,rural residential]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[appliances,commercial]","Fraction of New Bldg Components Shifted to Other Fuels[appliances,commercial]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[other component,commercial]","Fraction of New Bldg Components Shifted to Other Fuels[other component,commercial]",[0,1],"Building Electrification"),
    (True, "Industry Sector Fraction of Potential Additional CCS Achieved[cement and other carbonates,process emissions]","Industry Sector Fraction of Potential Additional CCS Achieved[cement and other carbonates,process emissions]",[0,0.5],"Industrial CCS"),
    (True, "Industry Sector Fraction of Potential Additional CCS Achieved[natural gas and petroleum systems,process emissions]","Industry Sector Fraction of Potential Additional CCS Achieved[natural gas and petroleum systems,process emissions]",[0,0.5],"Industrial CCS"),
    (True, "Industry Sector Fraction of Potential Additional CCS Achieved[iron and steel,process emissions]","Industry Sector Fraction of Potential Additional CCS Achieved[iron and steel,process emissions]",[0,0.5],"Industrial CCS"),
    (True, "Industry Sector Fraction of Potential Additional CCS Achieved[chemicals,process emissions]","Industry Sector Fraction of Potential Additional CCS Achieved[chemicals,process emissions]",[0,0.5],"Industrial CCS"),
    (True, "Industry Sector Fraction of Potential Additional CCS Achieved[other industries,process emissions]","Industry Sector Fraction of Potential Additional CCS Achieved[other industries,process emissions]",[0,0.5],"Industrial CCS"),
    (True, "Perc Subsidy for Elec Capacity Construction[solar PV es]","Perc Subsidy for Elec Capacity Construction[solar PV es]",[0,0.193],"Electricity PTC/ITC"),
    (True, "Percent of Travel Demand Shifted to Other Modes or Eliminated[passenger,LDVs]","Percent of Travel Demand Shifted to Other Modes or Eliminated[passenger,LDVs]",[0,0.2],"Passenger Mode Shifting"),
    (True, "Percent of Travel Demand Shifted to Other Modes or Eliminated[freight,HDVs]","Percent of Travel Demand Shifted to Other Modes or Eliminated[freight,HDVs]",[0,0.063],"Freight Logistics"),
    (True, "Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[cement and other carbonates]","Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[cement and other carbonates]",[0,0.05],"Material Efficiency"),
    (True, "Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[iron and steel]","Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[iron and steel]",[0,0.1],"Material Efficiency"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[passenger,LDVs]","Percentage Additional Improvement of Fuel Economy Std[passenger,LDVs]",[0,0.6],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[passenger,HDVs]","Percentage Additional Improvement of Fuel Economy Std[passenger,HDVs]",[0,0.2],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[passenger,aircraft]","Percentage Additional Improvement of Fuel Economy Std[passenger,aircraft]",[0,0.5],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[passenger,rail]","Percentage Additional Improvement of Fuel Economy Std[passenger,rail]",[0,0.2],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,LDVs]","Percentage Additional Improvement of Fuel Economy Std[freight,LDVs]",[0,0.6],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,HDVs]","Percentage Additional Improvement of Fuel Economy Std[freight,HDVs]",[0,0.3],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,aircraft]","Percentage Additional Improvement of Fuel Economy Std[freight,aircraft]",[0,0.5],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,rail]","Percentage Additional Improvement of Fuel Economy Std[freight,rail]",[0,0.25],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,ships]","Percentage Additional Improvement of Fuel Economy Std[freight,ships]",[0,0.8],"Fuel Economy Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,electricity if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,hard coal if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,natural gas if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,biomass if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,biomass if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,petroleum diesel if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,heavy or residual fuel oil if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates,LPG propane or butane if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems,electricity if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems,hard coal if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems,natural gas if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems,biomass if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems,biomass if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,electricity if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,hard coal if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,natural gas if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,petroleum diesel if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,heavy or residual fuel oil if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel,LPG propane or butane if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,electricity if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,hard coal if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,natural gas if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,petroleum diesel if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,heavy or residual fuel oil if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals,LPG propane or butane if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining,electricity if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining,hard coal if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining,natural gas if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining,petroleum diesel if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining,heavy or residual fuel oil if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[waste management,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[waste management,electricity if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture,electricity if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture,petroleum diesel if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture,heavy or residual fuel oil if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture,LPG propane or butane if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries,electricity if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries,hard coal if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries,natural gas if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries,petroleum diesel if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries,heavy or residual fuel oil if]",[0,0.17],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Increase in Transmission Capacity vs BAU","Percentage Increase in Transmission Capacity vs BAU",[0,1],"Grid Flexibility"),
    (True, "Reduction in E Use Allowed by Component Eff Std[heating,urban residential]","Reduction in E Use Allowed by Component Eff Std[heating,urban residential]",[0,0.111],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[heating,rural residential]","Reduction in E Use Allowed by Component Eff Std[heating,rural residential]",[0,0.111],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[heating,commercial]","Reduction in E Use Allowed by Component Eff Std[heating,commercial]",[0,0.159],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,urban residential]","Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,urban residential]",[0,0.136],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,rural residential]","Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,rural residential]",[0,0.136],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,commercial]","Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,commercial]",[0,0.133],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[envelope,urban residential]","Reduction in E Use Allowed by Component Eff Std[envelope,urban residential]",[0,0.75],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[envelope,rural residential]","Reduction in E Use Allowed by Component Eff Std[envelope,rural residential]",[0,0.75],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[envelope,commercial]","Reduction in E Use Allowed by Component Eff Std[envelope,commercial]",[0,0.75],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[lighting,urban residential]","Reduction in E Use Allowed by Component Eff Std[lighting,urban residential]",[0,0.2],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[lighting,rural residential]","Reduction in E Use Allowed by Component Eff Std[lighting,rural residential]",[0,0.2],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[lighting,commercial]","Reduction in E Use Allowed by Component Eff Std[lighting,commercial]",[0,0.2],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[appliances,urban residential]","Reduction in E Use Allowed by Component Eff Std[appliances,urban residential]",[0,0.142],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[appliances,rural residential]","Reduction in E Use Allowed by Component Eff Std[appliances,rural residential]",[0,0.142],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[appliances,commercial]","Reduction in E Use Allowed by Component Eff Std[appliances,commercial]",[0,0.142],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[other component,urban residential]","Reduction in E Use Allowed by Component Eff Std[other component,urban residential]",[0,0.11],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[other component,rural residential]","Reduction in E Use Allowed by Component Eff Std[other component,rural residential]",[0,0.11],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[other component,commercial]","Reduction in E Use Allowed by Component Eff Std[other component,commercial]",[0,0.11],"Building Codes and Appliance Standards"),
    (True, "Renewable Portfolio Std Percentage","Renewable Portfolio Std Percentage",[0,1],"100% Clean Electricity Standard"),
    (True, "Share of Preexisting Buildings Subject to Retrofitting[urban residential]","Share of Preexisting Buildings Subject to Retrofitting[urban residential]",[0,0.15],"Building Retrofitting"),
    (True, "Share of Preexisting Buildings Subject to Retrofitting[rural residential]","Share of Preexisting Buildings Subject to Retrofitting[rural residential]",[0,0.15],"Building Retrofitting"),
    (True, "Share of Preexisting Buildings Subject to Retrofitting[commercial]","Share of Preexisting Buildings Subject to Retrofitting[commercial]",[0,0.15],"Building Retrofitting"),
    (True, "Subsidy for Elec Production by Fuel[onshore wind es]","Subsidy for Elec Production by Fuel[onshore wind es]",[0,5],"Electricity PTC/ITC")
	
)

# Building the Policy List
# ------------------------
# Every policy, whether enabled or not, appears in a tuple called "PotentialPolicies" that was constructed above.
# Now we construct the actual list of policies to be included (named "Policies") by
# checking which of the policies have been enabled.

Policies = []
for PotentialPolicy in PotentialPolicies:
	if PotentialPolicy[Enabled]:
		Policies.append(PotentialPolicy)


# Exit with an error if no policies were enabled in the script.  We write the error to the output
# file because it's likely a user will run this without a console and won't be able to see the
# message produced by sys.exit()
if len(Policies) < 1:
	f = open(OutputScript, 'w')
	ErrorMessage = "Error: No policies were enabled in the Python script.  Before running the script, you must enable at least one policy."
	f.write(ErrorMessage)
	f.close()
	import sys
	sys.exit(ErrorMessage)


# Building the Groups List
# ------------------------
# We create a list of all the unique groups that are used by enabled policies.
Groups = []
for Policy in Policies:
	if Policy[Group] not in Groups:
		Groups.append(Policy[Group])


# Generate Vensim Command Script
# ------------------------------
# We begin by creating a new file to serve as the Vensim command script (overwriting
# any older version at that filename).  We then tell Vensim to load
# the model file, and we give it a RUNNAME that will be used for all runs.  (It is
# overwritten each run.)
f = open(OutputScript, 'w')
f.write('SPECIAL>LOADMODEL|"' + ModelFile + '"\n')
f.write("SIMULATE>RUNNAME|" + RunName + "\n")

# The following options may be useful in certain cases, but they may slow Vensim down
# or increase the odds that Vensim crashes during execution of a batch of runs (though
# it is hard to tell for sure).  These lines are usually best left commented out.
# f.write("SPECIAL>NOINTERACTION\n")
# f.write("SIMULATE>SAVELIST|" + OutputVarsFile + "\n")
f.write("\n")

def PerformRunsWithEnabledGroups():

	# First, we do a run with all of the groups disabled
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|||" + FirstYear + "|" + FinalYear + "|:")
	f.write("\tEnabledPolicyGroup=None")
	f.write("\tEnabledPolicies=None\n\n")

	# Next, we do a run with each group enabled in turn
	for EnabledGroup in Groups:

		# We create an empty string that we'll use to track the policies enabled in each group
		EnabledPolicies=""

		# We activate policies if their group name matches the currently enabled group
		for Policy in Policies:
			if Policy[Group] == EnabledGroup:
				f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
				# We add the policy to the EnabledPolicies string
				if len(EnabledPolicies) > 0:
					EnabledPolicies += ", "
				EnabledPolicies += Policy[ShortName]

		# We include a SETVAL instruction to select the correct policy implementation schedule file
		f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
		
		# We perform our run and log the output
		f.write("MENU>RUN|O\n")
		f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|+!||" + FirstYear + "|" + FinalYear + "|:")
		f.write("\tEnabledPolicyGroup=" + str(EnabledGroup))
		f.write("\tEnabledPolicies=" + EnabledPolicies + "\n\n")
	
	# Finally, we do a run with all of the policy groups enabled (a full policy case run)
	
	# We include a SETVAL instruction to select the correct policy implementation schedule file
	f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
	
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|+!||" + FirstYear + "|" + FinalYear + "|:")
	f.write("\tEnabledPolicyGroup=All")
	f.write("\tEnabledPolicies=All")
	f.write("\n")

	# We instruct Vensim to delete the .vdfx file, to prevent it from getting picked up by
	# sync software, such as DropBox or Google Drive.  If sync software locks the file,
	# Vensim won't be able to overwrite it on the next model run, ruining the batch.
	f.write("FILE>DELETE|" + RunName + ".vdfx")
	f.write("\n\n")
	
def PerformRunsWithDisabledGroups():

	# First, we do a run with all of the groups enabled
	for Policy in Policies:
		f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
	
	# We include a SETVAL instruction to select the correct policy implementation schedule file
	f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
	
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|||" + FirstYear + "|" + FinalYear + "|:")
	f.write("\tDisabledPolicyGroup=None")
	f.write("\tDisabledPolicies=None\n\n")

	# Next, we do a run with each group disabled in turn
	for DisabledGroup in Groups:

		# We create an empty string that we'll use to track the policies disabled in each group
		DisabledPolicies=""

		# We activate policies if their group name does not match the currently disabled group
		for Policy in Policies:
			if Policy[Group] != DisabledGroup:
				f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
			# Otherwise, we add the policy to the DisabledPolicies string
			else:
				if len(DisabledPolicies) > 0:
					DisabledPolicies += ", "
				DisabledPolicies += Policy[ShortName]
		
		# We include a SETVAL instruction to select the correct policy implementation schedule file
		f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
		
		# We perform our run and log the output
		f.write("MENU>RUN|O\n")
		f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|+!||" + FirstYear + "|" + FinalYear + "|:")
		f.write("\tDisabledPolicyGroup=" + str(DisabledGroup))
		f.write("\tDisabledPolicies=" + DisabledPolicies + "\n\n")
	
	# Finally, we do a run with all of the groups disabled (a BAU case run)
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|+!||" + FirstYear + "|" + FinalYear + "|:")
	f.write("\tDisabledPolicyGroup=All")
	f.write("\tDisabledPolicies=All")
	f.write("\n")

	# We instruct Vensim to delete the .vdfx file, to prevent it from getting picked up by
	# sync software, such as DropBox or Google Drive.  If sync software locks the file,
	# Vensim won't be able to overwrite it on the next model run, ruining the batch.
	f.write("FILE>DELETE|" + RunName + ".vdfx")
	f.write("\n\n")
	
if EnableOrDisableGroups == "Enable":
	PerformRunsWithEnabledGroups()
else:
	PerformRunsWithDisabledGroups()

# We are done writing the Vensim command script and therefore close the file.
f.close()
