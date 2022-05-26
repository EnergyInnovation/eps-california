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
FirstYear = "2020" # The first year you wish to include in the output file (cannot be prior to first simulated year)
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
PolicySchedule = 2 # The number of the policy implementation schedule file to be used (in InputData/plcy-schd/FoPITY)


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
    (True, "Additional Minimum Required EV Sales Percentage[freight,motorbikes]","Additional Minimum Required EV Sales Percentage[freight,motorbikes]",[0,1],"California HDV Rules"),
    (True, "Boolean Rebate Program for Efficient Components[heating]","Boolean Rebate Program for Efficient Components[heating]",[0,1],"Building Codes and Appliance Standards"),
    (True, "Boolean Rebate Program for Efficient Components[cooling and ventilation]","Boolean Rebate Program for Efficient Components[cooling and ventilation]",[0,1],"Building Codes and Appliance Standards"),
    (True, "Boolean Rebate Program for Efficient Components[appliances]","Boolean Rebate Program for Efficient Components[appliances]",[0,1],"Building Codes and Appliance Standards"),
    (True, "Electricity Sector Fraction of Potential Additional CCS Achieved[petroleum es]","Electricity Sector Fraction of Potential Additional CCS Achieved[petroleum es]",[0,1],"Power Sector Gas Regs"),
    (True, "Electricity Sector Fraction of Potential Additional CCS Achieved[natural gas peaker es]","Electricity Sector Fraction of Potential Additional CCS Achieved[natural gas peaker es]",[0,1],"Power Sector Gas Regs"),
    (True, "Fraction of Additional Demand Response Potential Achieved","Fraction of Additional Demand Response Potential Achieved",[0,1],"Grid Flexibility"),
    (True, "Fraction of Additional Grid Battery Storage Potential Achieved","Fraction of Additional Grid Battery Storage Potential Achieved",[0,1],"Grid Flexibility"),
    (True, "Fraction of Afforestation and Reforestation Achieved","Fraction of Afforestation and Reforestation Achieved",[0,1],"Afforestation and Reforestation"),
    (True, "Fraction of Cement Measures Achieved","Fraction of Cement Measures Achieved",[0,1],"Cement Clinker Substitution"),
    (True, "Fraction of Cropland and Rice Measures Achieved","Fraction of Cropland and Rice Measures Achieved",[0,1],"Cropland Measures"),
    (True, "Fraction of F Gas Destruction Achieved","Fraction of F Gas Destruction Achieved",[0,1],"F-Gas Policies"),
    (True, "Fraction of F Gas Inspct Maint Retrofit Achieved","Fraction of F Gas Inspct Maint Retrofit Achieved",[0,1],"F-Gas Policies"),
    (True, "Fraction of F Gas Recovery Achieved","Fraction of F Gas Recovery Achieved",[0,1],"F-Gas Policies"),
    (True, "Fraction of F Gas Substitution Achieved","Fraction of F Gas Substitution Achieved",[0,1],"F-Gas Policies"),
    (True, "Fraction of Hydrogen Production Pathways Shifted","Fraction of Hydrogen Production Pathways Shifted",[0,1],"Hydrogen Electrolysis"),
    (True, "Fraction of Improved Forest Management Achieved","Fraction of Improved Forest Management Achieved",[0,1],"Forest Management"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture and forestry 01T03,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture and forestry 01T03,electricity if]",[0,0.9],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining 05,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining 05,electricity if]",[0,0.92],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining 05,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining 05,hydrogen if]",[0,0.08],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[oil and gas extraction 06,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[oil and gas extraction 06,electricity if]",[0,0.92],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[oil and gas extraction 06,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[oil and gas extraction 06,hydrogen if]",[0,0.08],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other mining and quarrying 07T08,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other mining and quarrying 07T08,electricity if]",[0,0.92],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other mining and quarrying 07T08,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other mining and quarrying 07T08,hydrogen if]",[0,0.08],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[food beverage and tobacco 10T12,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[food beverage and tobacco 10T12,electricity if]",[0,0.88],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[food beverage and tobacco 10T12,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[food beverage and tobacco 10T12,hydrogen if]",[0,0.12],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[textiles apparel and leather 13T15,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[textiles apparel and leather 13T15,electricity if]",[0,0.92],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[textiles apparel and leather 13T15,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[textiles apparel and leather 13T15,hydrogen if]",[0,0.08],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[wood products 16,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[wood products 16,electricity if]",[0,0.92],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[wood products 16,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[wood products 16,hydrogen if]",[0,0.08],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[pulp paper and printing 17T18,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[pulp paper and printing 17T18,electricity if]",[0,0.97],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[pulp paper and printing 17T18,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[pulp paper and printing 17T18,hydrogen if]",[0,0.03],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[refined petroleum and coke 19,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[refined petroleum and coke 19,electricity if]",[0,0.48],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[refined petroleum and coke 19,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[refined petroleum and coke 19,hydrogen if]",[0,0.52],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals 20,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals 20,electricity if]",[0,0.47],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals 20,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals 20,hydrogen if]",[0,0.53],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[rubber and plastic products 22,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[rubber and plastic products 22,electricity if]",[0,0.47],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[rubber and plastic products 22,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[rubber and plastic products 22,hydrogen if]",[0,0.53],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[glass and glass products 231,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[glass and glass products 231,electricity if]",[0,0.92],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[glass and glass products 231,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[glass and glass products 231,hydrogen if]",[0,0.08],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other nonmetallic minerals 239,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other nonmetallic minerals 239,electricity if]",[0,0.22],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other nonmetallic minerals 239,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other nonmetallic minerals 239,hydrogen if]",[0,0.78],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel 241,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel 241,electricity if]",[0,0.29],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel 241,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel 241,hydrogen if]",[0,0.71],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other metals 242,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other metals 242,electricity if]",[0,0.44],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other metals 242,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other metals 242,hydrogen if]",[0,0.56],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[metal products except machinery and vehicles 25,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[metal products except machinery and vehicles 25,electricity if]",[0,0.92],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[metal products except machinery and vehicles 25,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[metal products except machinery and vehicles 25,hydrogen if]",[0,0.08],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[computers and electronics 26,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[computers and electronics 26,electricity if]",[0,0.92],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[computers and electronics 26,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[computers and electronics 26,hydrogen if]",[0,0.08],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[appliances and electrical equipment 27,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[appliances and electrical equipment 27,electricity if]",[0,0.92],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[appliances and electrical equipment 27,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[appliances and electrical equipment 27,hydrogen if]",[0,0.08],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other machinery 28,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other machinery 28,electricity if]",[0,0.94],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other machinery 28,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other machinery 28,hydrogen if]",[0,0.06],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[road vehicles 29,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[road vehicles 29,electricity if]",[0,0.94],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[road vehicles 29,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[road vehicles 29,hydrogen if]",[0,0.06],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[nonroad vehicles 30,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[nonroad vehicles 30,electricity if]",[0,0.94],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[nonroad vehicles 30,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[nonroad vehicles 30,hydrogen if]",[0,0.06],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other manufacturing 31T33,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other manufacturing 31T33,electricity if]",[0,0.92],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[other manufacturing 31T33,hydrogen if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[other manufacturing 31T33,hydrogen if]",[0,0.08],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[energy pipelines and gas processing 352T353,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[energy pipelines and gas processing 352T353,electricity if]",[0,0.9],"Industrial Fuel Switching"),
    (True, "Fraction of Industrial Fuel Use Shifted to Other Fuels[construction 41T43,electricity if]","Fraction of Industrial Fuel Use Shifted to Other Fuels[construction 41T43,electricity if]",[0,0.9],"Industrial Fuel Switching"),
    (True, "Fraction of Livestock Measures Achieved","Fraction of Livestock Measures Achieved",[0,1],"Livestock Measures"),
    (True, "Fraction of Methane Capture Opportunities Achieved[coal mining 05]","Fraction of Methane Capture Opportunities Achieved[coal mining 05]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Capture Opportunities Achieved[oil and gas extraction 06]","Fraction of Methane Capture Opportunities Achieved[oil and gas extraction 06]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Capture Opportunities Achieved[energy pipelines and gas processing 352T353]","Fraction of Methane Capture Opportunities Achieved[energy pipelines and gas processing 352T353]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Capture Opportunities Achieved[water and waste 36T39]","Fraction of Methane Capture Opportunities Achieved[water and waste 36T39]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Destruction Opportunities Achieved[coal mining 05]","Fraction of Methane Destruction Opportunities Achieved[coal mining 05]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Destruction Opportunities Achieved[oil and gas extraction 06]","Fraction of Methane Destruction Opportunities Achieved[oil and gas extraction 06]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Destruction Opportunities Achieved[energy pipelines and gas processing 352T353]","Fraction of Methane Destruction Opportunities Achieved[energy pipelines and gas processing 352T353]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of Methane Destruction Opportunities Achieved[water and waste 36T39]","Fraction of Methane Destruction Opportunities Achieved[water and waste 36T39]",[0,1],"Methane Capture and Destruction"),
    (True, "Fraction of N2O Abatement Achieved","Fraction of N2O Abatement Achieved",[0,1],"N2O Abatement"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[heating,urban residential]","Fraction of New Bldg Components Shifted to Other Fuels[heating,urban residential]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[heating,rural residential]","Fraction of New Bldg Components Shifted to Other Fuels[heating,rural residential]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[heating,commercial]","Fraction of New Bldg Components Shifted to Other Fuels[heating,commercial]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[appliances,urban residential]","Fraction of New Bldg Components Shifted to Other Fuels[appliances,urban residential]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[appliances,rural residential]","Fraction of New Bldg Components Shifted to Other Fuels[appliances,rural residential]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[appliances,commercial]","Fraction of New Bldg Components Shifted to Other Fuels[appliances,commercial]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[other component,urban residential]","Fraction of New Bldg Components Shifted to Other Fuels[other component,urban residential]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[other component,rural residential]","Fraction of New Bldg Components Shifted to Other Fuels[other component,rural residential]",[0,1],"Building Electrification"),
    (True, "Fraction of New Bldg Components Shifted to Other Fuels[other component,commercial]","Fraction of New Bldg Components Shifted to Other Fuels[other component,commercial]",[0,1],"Building Electrification"),
    (True, "Industry Sector Fraction of Potential Additional CCS Achieved[chemicals 20,process emissions]","Industry Sector Fraction of Potential Additional CCS Achieved[chemicals 20,process emissions]",[0,0.5],"Industrial CCS"),
    (True, "Industry Sector Fraction of Potential Additional CCS Achieved[cement and other nonmetallic minerals 239,process emissions]","Industry Sector Fraction of Potential Additional CCS Achieved[cement and other nonmetallic minerals 239,process emissions]",[0,0.5],"Industrial CCS"),
    (True, "Industry Sector Fraction of Potential Additional CCS Achieved[iron and steel 241,process emissions]","Industry Sector Fraction of Potential Additional CCS Achieved[iron and steel 241,process emissions]",[0,0.5],"Industrial CCS"),
    (True, "Percent of Travel Demand Shifted to Other Modes or Eliminated[passenger,LDVs]","Percent of Travel Demand Shifted to Other Modes or Eliminated[passenger,LDVs]",[0,0.26],"Passenger Mode Shifting"),
    (True, "Percent Reduction in Fossil Fuel Exports[petroleum gasoline]","Percent Reduction in Fossil Fuel Exports[petroleum gasoline]",[0,0.8567],"Reduction in Fossil Fuel Exports"),
    (True, "Percent Reduction in Fossil Fuel Exports[petroleum diesel]","Percent Reduction in Fossil Fuel Exports[petroleum diesel]",[0,0.8567],"Reduction in Fossil Fuel Exports"),
    (True, "Percent Reduction in Fossil Fuel Exports[crude oil]","Percent Reduction in Fossil Fuel Exports[crude oil]",[0,0.8567],"Reduction in Fossil Fuel Exports"),
    (True, "Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[cement and other nonmetallic minerals 239]","Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[cement and other nonmetallic minerals 239]",[0,0.1],"Material Efficiency"),
    (True, "Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[iron and steel 241]","Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[iron and steel 241]",[0,0.15],"Reduction in Industry Product Demand"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[passenger,LDVs]","Percentage Additional Improvement of Fuel Economy Std[passenger,LDVs]",[0,0.6],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[passenger,HDVs]","Percentage Additional Improvement of Fuel Economy Std[passenger,HDVs]",[0,0.5],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[passenger,aircraft]","Percentage Additional Improvement of Fuel Economy Std[passenger,aircraft]",[0,0.6],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[passenger,rail]","Percentage Additional Improvement of Fuel Economy Std[passenger,rail]",[0,0.25],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,LDVs]","Percentage Additional Improvement of Fuel Economy Std[freight,LDVs]",[0,0.5],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,HDVs]","Percentage Additional Improvement of Fuel Economy Std[freight,HDVs]",[0,0.5],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,aircraft]","Percentage Additional Improvement of Fuel Economy Std[freight,aircraft]",[0,0.6],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,rail]","Percentage Additional Improvement of Fuel Economy Std[freight,rail]",[0,0.25],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,ships]","Percentage Additional Improvement of Fuel Economy Std[freight,ships]",[0,0.8],"Fuel Economy Standards"),
    (True, "Percentage Additional Improvement of Fuel Economy Std[freight,motorbikes]","Percentage Additional Improvement of Fuel Economy Std[freight,motorbikes]",[0,0.5],"Fuel Economy Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture and forestry 01T03,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture and forestry 01T03,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture and forestry 01T03,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture and forestry 01T03,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture and forestry 01T03,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture and forestry 01T03,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture and forestry 01T03,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture and forestry 01T03,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture and forestry 01T03,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture and forestry 01T03,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining 05,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining 05,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining 05,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining 05,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining 05,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining 05,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining 05,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining 05,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining 05,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining 05,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[oil and gas extraction 06,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[oil and gas extraction 06,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[oil and gas extraction 06,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[oil and gas extraction 06,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[oil and gas extraction 06,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[oil and gas extraction 06,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[oil and gas extraction 06,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[oil and gas extraction 06,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other mining and quarrying 07T08,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other mining and quarrying 07T08,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other mining and quarrying 07T08,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other mining and quarrying 07T08,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other mining and quarrying 07T08,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other mining and quarrying 07T08,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other mining and quarrying 07T08,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other mining and quarrying 07T08,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[food beverage and tobacco 10T12,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[textiles apparel and leather 13T15,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[wood products 16,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[pulp paper and printing 17T18,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[refined petroleum and coke 19,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[refined petroleum and coke 19,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[refined petroleum and coke 19,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[refined petroleum and coke 19,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[refined petroleum and coke 19,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[refined petroleum and coke 19,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[refined petroleum and coke 19,biomass if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[refined petroleum and coke 19,biomass if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[refined petroleum and coke 19,crude oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[refined petroleum and coke 19,crude oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals 20,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[rubber and plastic products 22,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[rubber and plastic products 22,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[rubber and plastic products 22,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[rubber and plastic products 22,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[rubber and plastic products 22,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[rubber and plastic products 22,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[rubber and plastic products 22,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[rubber and plastic products 22,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[rubber and plastic products 22,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[rubber and plastic products 22,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[glass and glass products 231,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[glass and glass products 231,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[glass and glass products 231,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[glass and glass products 231,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[glass and glass products 231,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[glass and glass products 231,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[glass and glass products 231,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[glass and glass products 231,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other nonmetallic minerals 239,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel 241,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other metals 242,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[metal products except machinery and vehicles 25,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[metal products except machinery and vehicles 25,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[metal products except machinery and vehicles 25,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[metal products except machinery and vehicles 25,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[metal products except machinery and vehicles 25,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[metal products except machinery and vehicles 25,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[metal products except machinery and vehicles 25,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[metal products except machinery and vehicles 25,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[computers and electronics 26,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[computers and electronics 26,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[computers and electronics 26,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[computers and electronics 26,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[computers and electronics 26,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[computers and electronics 26,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[computers and electronics 26,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[computers and electronics 26,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[appliances and electrical equipment 27,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[appliances and electrical equipment 27,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[appliances and electrical equipment 27,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[appliances and electrical equipment 27,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[appliances and electrical equipment 27,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[appliances and electrical equipment 27,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[appliances and electrical equipment 27,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[appliances and electrical equipment 27,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other machinery 28,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other machinery 28,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other machinery 28,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other machinery 28,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other machinery 28,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other machinery 28,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other machinery 28,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other machinery 28,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other machinery 28,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other machinery 28,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[road vehicles 29,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[nonroad vehicles 30,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,hard coal if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,hard coal if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[other manufacturing 31T33,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[energy pipelines and gas processing 352T353,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[energy pipelines and gas processing 352T353,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[water and waste 36T39,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[water and waste 36T39,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[construction 41T43,electricity if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[construction 41T43,electricity if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[construction 41T43,natural gas if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[construction 41T43,natural gas if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[construction 41T43,petroleum diesel if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[construction 41T43,petroleum diesel if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[construction 41T43,heavy or residual fuel oil if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[construction 41T43,heavy or residual fuel oil if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Improvement in Eqpt Efficiency Standards above BAU[construction 41T43,LPG propane or butane if]","Percentage Improvement in Eqpt Efficiency Standards above BAU[construction 41T43,LPG propane or butane if]",[0,0.14],"Industrial Energy Efficiency Standards"),
    (True, "Percentage Increase in Transmission Capacity vs BAU","Percentage Increase in Transmission Capacity vs BAU",[0,1],"Grid Flexibility"),
    (True, "Reduction in E Use Allowed by Component Eff Std[heating,urban residential]","Reduction in E Use Allowed by Component Eff Std[heating,urban residential]",[0,0.11],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[heating,rural residential]","Reduction in E Use Allowed by Component Eff Std[heating,rural residential]",[0,0.11],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[heating,commercial]","Reduction in E Use Allowed by Component Eff Std[heating,commercial]",[0,0.159],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,urban residential]","Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,urban residential]",[0,0.136],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,rural residential]","Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,rural residential]",[0,0.136],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,commercial]","Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,commercial]",[0,0.133],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[envelope,urban residential]","Reduction in E Use Allowed by Component Eff Std[envelope,urban residential]",[0,0.25],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[envelope,rural residential]","Reduction in E Use Allowed by Component Eff Std[envelope,rural residential]",[0,0.25],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[envelope,commercial]","Reduction in E Use Allowed by Component Eff Std[envelope,commercial]",[0,0.25],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[lighting,urban residential]","Reduction in E Use Allowed by Component Eff Std[lighting,urban residential]",[0,0.2],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[lighting,rural residential]","Reduction in E Use Allowed by Component Eff Std[lighting,rural residential]",[0,0.2],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[lighting,commercial]","Reduction in E Use Allowed by Component Eff Std[lighting,commercial]",[0,0.2],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[appliances,urban residential]","Reduction in E Use Allowed by Component Eff Std[appliances,urban residential]",[0,0.141],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[appliances,rural residential]","Reduction in E Use Allowed by Component Eff Std[appliances,rural residential]",[0,0.141],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[appliances,commercial]","Reduction in E Use Allowed by Component Eff Std[appliances,commercial]",[0,0.141],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[other component,urban residential]","Reduction in E Use Allowed by Component Eff Std[other component,urban residential]",[0,0.11],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[other component,rural residential]","Reduction in E Use Allowed by Component Eff Std[other component,rural residential]",[0,0.11],"Building Codes and Appliance Standards"),
    (True, "Reduction in E Use Allowed by Component Eff Std[other component,commercial]","Reduction in E Use Allowed by Component Eff Std[other component,commercial]",[0,0.11],"Building Codes and Appliance Standards"),
    (True, "Renewable Portfolio Std Percentage","Renewable Portfolio Std Percentage",[0,1],"100% Clean Electricity Standard"),
    (True, "Subsidy for Elec Production by Fuel[nuclear es,preexisting retiring]","Subsidy for Elec Production by Fuel[nuclear es,preexisting retiring]",[0,11],"Electricity PTC/ITC"),
    (True, "Subsidy for Elec Production by Fuel[onshore wind es,preexisting retiring]","Subsidy for Elec Production by Fuel[onshore wind es,preexisting retiring]",[0,5],"Electricity PTC/ITC"),
    (True, "Subsidy for Elec Production by Fuel[onshore wind es,newly built]","Subsidy for Elec Production by Fuel[onshore wind es,newly built]",[0,5],"Electricity PTC/ITC")

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
