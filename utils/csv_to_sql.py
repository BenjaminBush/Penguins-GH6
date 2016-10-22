import csv
import datetime
from dateutil.parser import parse
from value_maps import ethnicity, war_participated
from api.models import Client
from api.models import Services

def sync_client():
    with open('sample_data/client.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        ethnicity_funct = lambda k: [name for name in ethnicity.keys() if int(k[name])]
        war_participated_funct = lambda k: [war_participated[name] for name in war_participated.keys() if int(k[name])]
        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "uuid": row["UUID"],
                "first_name": row["First_Name"],
                "middle_name": row["Middle_Name"],
                "last_name": row["Last_Name"],
                "social_security": row["SSN"],
                "date_of_birth": fmt_date(row["DOB"]),
                "gender": int(row["Gender"]) if row['Gender'] else None,
                "veteran": int(row["VeteranStatus"]) if row['VeteranStatus'] else None,
                "year_entered": int(row["YearEnteredService"]) if row['YearEnteredService'] else None,
                "year_exited": int(row["YearSeparated"]) if row['YearSeparated'] else None,
                "military_branch": int(row["MilitaryBranch"]) if row['MilitaryBranch'] else None,
                "discharge_status": row["Discharge_Status"],
                "date_created": fmt_datetime(row["Date_Created"]),
                "date_updated": fmt_datetime(row["DateUpdated"]),
                "associate_id": row["UserID"],
                "ethnicity": ethnicity[ethnicity_funct(row)[0]],
                "war_participated": war_participated_funct(row)
            }

            bulk_create.append(Client(**csv2db_client))

def sync_disabilities():
    with open('sample_data/disabilities.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        cast_int = lambda k: int(k) if k else None

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "disabilities_id":row["DisabilitiesID"],
                "project_entry_id":row["ProjectEntryID"],
                "personal_id":row["PersonalID"],
                "information_date":fmt_date(row["InformationDate"]),
                "disability_type":cast_int(row["DisabilityType"]),
                "indefinite_and_impairs":cast_int(row["IndefiniteAndImpairs"]),
                "documentation_on_file":cast_int(row["DocumentationOnFile"]),
                "receiving_services":cast_int(row["ReceivingServices"]),
                "path_how_confirmed":cast_int(row["PATHHowConfirmed"]),
                "data_collection_stage":cast_int(row["DataCollectionStage"]),
                "date_created":cast_int(row["DateCreated"]),
                "date_updated":cast_int(row["DateUpdated"]),
                "associate_id":cast_int(row["UserID"]),
                "":row["DateDeleted"],
                "":row["ExportID"]
            }
            bulk_create.append(Client(**csv2db_client))

def sync_employmenteducation():
    with open('sample_data/employmenteducation.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

                csv2db_client = {
                    "personal_id" : row["PersonalID"],
                    "project_entry_id" : row["ProjectEntryID"],
                    "services_id" : row["ServicesID"],
                    "date_provided" : fmt_date(row["DateProvided"]),
                    "record_type" : int(row["RecordType"]) if row['RecordType'] else None,
                    "type_provided" : int(row["TypeProvided"]) if row['TypeProvided'] else None,
                    "other_type_provided" : int(row["OtherTypeProvided"]) if row['OtherTypeProvided'] else None,
                    "sub_type_provided" = int(row["SubTypeProvided"]) if row['SubTypeProvided'] else None,
                    "fa_amount" : int(row["FAAmount"]) if row['FAAmount'] else None,
                    "referral_outcome" = row["ReferralOutcome"],
                    "date_created" : fmt_datetime(row["DateCreated"]),
                    "date_updated" : fmt_datetime(row["DateUpdated"]),
                    "associate_id" : row["UserID"]
                }

                bulk_create.append(Client(**csv2db_client))

            csv2db_client = {
                "":row["EmploymentEducationID"],
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["InformationDate"],
                "":row["LastGradeCompleted"],
                "":row["SchoolStatus"],
                "":row["Employed"],
                "":row["EmploymentType"],
                "":row["NotEmployedReason"],
                "":row["DataCollectionStage"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"]
            }
            bulk_create.append(Client(**csv2db_client))

def sync_enrollment():
    with open('sample_data/enrollment.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["ProjectID"],
                "":row["EntryDate"],
                "":row["HouseholdID"],
                "":row["RelationshipToHoH"],
                "":row["ResidencePrior"],
                "":row["OtherResidencePrior"],
                "":row["ResidencePriorLengthOfStay"],
                "":row["DisablingCondition"],
                "":row["EntryFromStreetESSH"],
                "":row["DateToStreetESSH"],
                "":row["TimesHomelessPastThreeYears"],
                "":row["MonthsHomelessPastThreeYears"],
                "":row["HousingStatus"],
                "":row["DateOfEngagement"],
                "":row["InPermanentHousing"],
                "":row["ResidentialMoveInDate"],
                "":row["DateOfPATHStatus"],
                "":row["ClientEnrolledInPATH"],
                "":row["ReasonNotEnrolled"],
                "":row["WorstHousingSituation"],
                "":row["PercentAMI"],
                "":row["LastPermanentStreet"],
                "":row["LastPermanentCity"],
                "":row["LastPermanentState"],
                "":row["LastPermanentZIP"],
                "":row["AddressDataQuality"],
                "":row["DateOfBCPStatus"],
                "":row["FYSBYouth"],
                "":row["ReasonNoServices"],
                "":row["SexualOrientation"],
                "":row["FormerWardChildWelfare"],
                "":row["ChildWelfareYears"],
                "":row["ChildWelfareMonths"],
                "":row["FormerWardJuvenileJustice"],
                "":row["JuvenileJusticeYears"],
                "":row["JuvenileJusticeMonths"],
                "":row["HouseholdDynamics"],
                "":row["SexualOrientationGenderIDYouth"],
                "":row["SexualOrientationGenderIDFam"],
                "":row["HousingIssuesYouth"],
                "":row["HousingIssuesFam"],
                "":row["SchoolEducationalIssuesYouth"],
                "":row["SchoolEducationalIssuesFam"],
                "":row["UnemploymentYouth"],
                "":row["UnemploymentFam"],
                "":row["MentalHealthIssuesYouth"],
                "":row["MentalHealthIssuesFam"],
                "":row["HealthIssuesYouth"],
                "":row["HealthIssuesFam"],
                "":row["PhysicalDisabilityYouth"],
                "":row["PhysicalDisabilityFam"],
                "":row["MentalDisabilityYouth"],
                "":row["MentalDisabilityFam"],
                "":row["AbuseAndNeglectYouth"],
                "":row["AbuseAndNeglectFam"],
                "":row["AlcoholDrugAbuseYouth"],
                "":row["AlcoholDrugAbuseFam"],
                "":row["InsufficientIncome"],
                "":row["ActiveMilitaryParent"],
                "":row["IncarceratedParent"],
                "":row["IncarceratedParentStatus"],
                "":row["ReferralSource"],
                "":row["CountOutreachReferralApproaches"],
                "":row["ExchangeForSex"],
                "":row["ExchangeForSexPastThreeMonths"],
                "":row["CountOfExchangeForSex"],
                "":row["AskedOrForcedToExchangeForSex"],
                "":row["AskedOrForcedToExchangeForSexPastThreeMonths"],
                "":row["WorkPlaceViolenceThreats"],
                "":row["WorkplacePromiseDifference"],
                "":row["CoercedToContinueWork"],
                "":row["LaborExploitPastThreeMonths"],
                "":row["HPScreeningScore"],
                "":row["VAMCStation"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"]
            }
            bulk_create.append(Client(**csv2db_client))

def sync_exit():
    with open('sample_data/exit.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "ExitID"":row[""],
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["ExitDate"],
                "":row["Destination"],
                "":row["OtherDestination"],
                "":row["AssessmentDisposition"],
                "":row["OtherDisposition"],
                "":row["HousingAssessment"],
                "":row["SubsidyInformation"],
                "":row["ConnectionWithSOAR"],
                "":row["WrittenAftercarePlan"],
                "":row["AssistanceMainstreamBenefits"],
                "":row["PermanentHousingPlacement"],
                "":row["TemporaryShelterPlacement"],
                "":row["ExitCounseling"],
                "":row["FurtherFollowUpServices"],
                "":row["ScheduledFollowUpContacts"],
                "":row["ResourcePackage"],
                "":row["OtherAftercarePlanOrAction"],
                "":row["ProjectCompletionStatus"],
                "":row["EarlyExitReason"],
                "":row["FamilyReunificationAchieved"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"]
            }
            bulk_create.append()

def sync_funder():
    with open('sample_data/funder.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "":row["ExitID"],
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["ExitDate"],
                "":row["Destination"],
                "":row["OtherDestination"],
                "":row["AssessmentDisposition"],
                "":row["OtherDisposition"],
                "":row["HousingAssessment"],
                "":row["SubsidyInformation"],
                "":row["ConnectionWithSOAR"],
                "":row["WrittenAftercarePlan"],
                "":row["AssistanceMainstreamBenefits"],
                "":row["PermanentHousingPlacement"],
                "":row["TemporaryShelterPlacement"],
                "":row["ExitCounseling"],
                "":row["FurtherFollowUpServices"],
                "":row["ScheduledFollowUpContacts"],
                "":row["ResourcePackage"],
                "":row["OtherAftercarePlanOrAction"],
                "":row["ProjectCompletionStatus"],
                "":row["EarlyExitReason"],
                "":row["FamilyReunificationAchieved"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"]
            }
            bulk_create.append()

def sync_health_and_dv():
    with open('sample_data/healthanddv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "":row["HealthAndDVID"],
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["InformationDate"],
                "":row["DomesticViolenceVictim"],
                "":row["WhenOccurred"],
                "":row["CurrentlyFleeing"],
                "":row["GeneralHealthStatus"],
                "":row["DentalHealthStatus"],
                "":row["MentalHealthStatus"],
                "":row["PregnancyStatus"],
                "":row["DueDate"],
                "":row["DataCollectionStage"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"]
            }
            bulk_create.append()

def sync_income_benefits():
    with open('sample_data/income_benefits') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create = []

        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        cast_int = lambda k: int(k) if k else None
        cast_bool = lambda k : bool(k) if k else None
        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "income_benefits_id":row["IncomeBenefitsID"],
                "project_entry_id":row["ProjectEntryID"],
                "personal_id":row["PersonalID"],
                "information_date":fmt_date(row["InformationDate"],)
                "income_from_any_source":cast_int(row["IncomeFromAnySource"]),
                "total_monthly_income":cast_int(row["TotalMonthlyIncome"]),
                "earned":cast_bool(row["Earned"]),
                "earned_amount":cast_int(row["EarnedAmount"]),
                "unemployment":cast_bool(row["Unemployment"]),
                "unemployment_amount":cast_int(row["UnemploymentAmount"]),
                "ssi":cast_bool(row["SSI"]),
                "ssi_amount":cast_int(row["SSIAmount"]),
                "ssdi":cast_bool(row["SSDI"]),
                "ssdi_amont":cast_bool(row["SSDIAmount"]),
                "va_disability_service":cast_bool(row["VADisabilityService"]),
                "va_disability_service_amount":cast_int(row["VADisabilityServiceAmount"]),
                "va_disability_non_service":cast_bool(row["VADisabilityNonService"]),
                "va_disability_non_service_amount":cast_int(row["VADisabilityNonServiceAmount"]),
                "private_disability":cast_bool(row["PrivateDisability"]),
                "private_disability_amount":cast_int(row["PrivateDisabilityAmount"]),
                "workers_comp":cast_bool(row["WorkersComp"]),
                "workers_comp_amount":cast_int(row["WorkersCompAmount"]),
                "tanf":cast_bool(row["TANF"]),
                "tanf_amount":cast_int(row["TANFAmount"]),
                "ga":cast_bool(row["GA"]),
                "ga_amount":cast_int(row["GAAmount"]),
                "soc_sec_retirement":cast_bool(row["SocSecRetirement"]),
                "soc_sec_retirement_amount":cast_int(row["SocSecRetirementAmount"]),
                "pension":cast_bool(row["Pension"]),
                "pension_amount":cast_int(row["PensionAmount"]),
                "child_support":cast_bool(row["ChildSupport"]),
                "child_support_amount":cast_int(row["ChildSupportAmount"]),
                "alimony":cast_bool(row["Alimony"])
                "alimony_amount":cast_int(row["AlimonyAmount"])
                "other_income_source":cast_bool(row["OtherIncomeSource"]),
                "other_income_source_amount":cast_int(row["OtherIncomeAmount"]),
                "other_income_source_identify":row["OtherIncomeSourceIdentify"],
                "benefits_from_any_source":cast_bool(row["BenefitsFromAnySource"]),
                "snap":cast_bool(row["SNAP"]),
                "wic":cast_bool(row["WIC"]),
                "tanf_child_care":cast_bool(row["TANFChildCare"]),
                "tanf_transportation":cast_bool(row["TANFTransportation"]),
                "other_tanf":cast_bool(row["OtherTANF"]),
                "rental_assistance_ongoing":cast_bool(row["RentalAssistanceOngoing"]),
                "rental_assistance_temp":cast_bool(row["RentalAssistanceTemp"]),
                "other_benefits_source":cast_bool(row["OtherBenefitsSource"]),
                "other_benefits_source_identify":row["OtherBenefitsSourceIdentify"],
                "insurance_from_any_source":cast_bool(row["InsuranceFromAnySource"]),
                "medicaid":cast_bool(row["Medicaid"]),
                "no_medicaid_reason":cast_int(row["NoMedicaidReason"]),
                "medicare":cast_bool(row["Medicare"])
                "no_medicare_reason":cast_int(row["NoMedicareReason"]),
                "schip":cast_bool(row["SCHIP"]),
                "no_schip_reason":row["NoSCHIPReason"],
                "va_medical_services":cast_bool(row["VAMedicalServices"]),
                "no_va_med_reason":row["NoVAMedReason"],
                "employer_provided":cast_bool(row["EmployerProvided"]),
                "no_employer_provided_reason":row["NoEmployerProvidedReason"],
                "cobra":cast_bool(row["COBRA"]),
                "no_cobra_reason":row["NoCOBRAReason"],
                "private_pay":cast_bool(row["PrivatePay"]),
                "no_private_pay_reason":row["NoPrivatePayReason"],
                "state_health_ins":row["StateHealthIns"],
                "no_state_health_ins_reason":row["NoStateHealthInsReason"],
                "hiv_aids_assistance":cast_bool(row["HIVAIDSAssistance"]),
                "no_hiv_aids_assistance_reason":row["NoHIVAIDSAssistanceReason"],
                "adap":cast_bool(row["ADAP"]),
                "no_adap_reason":row["NoADAPReason"],
                "data_collection_stage":cast_int(row["DataCollectionStage"]),
                "date_created":fmt_datetime(row["DateCreated"]),
                "date_updated":fmt_datetime(row["DateUpdated"]),
                "associate_id":row["UserID"]
            }

            bulk_create.append(Client(**csv2db_client))


def sync_services():
    with open('sample_data/services.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create = []
        #Format functions where applicable
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "personal_id" : row["PersonalID"],
                "project_entry_id" : row["ProjectEntryID"],
                "services_id" : row["ServicesID"],
                "date_provided" : fmt_date(row["DateProvided"]),
                "record_type" : int(row["RecordType"]) if row['RecordType'] else None,
                "type_provided" : int(row["TypeProvided"]) if row['TypeProvided'] else None,
                "other_type_provided" : int(row["OtherTypeProvided"]) if row['OtherTypeProvided'] else None,
                "sub_type_provided" = int(row["SubTypeProvided"]) if row['SubTypeProvided'] else None,
                "fa_amount" : int(row["FAAmount"]) if row['FAAmount'] else None,
                "referral_outcome" = row["ReferralOutcome"],
                "date_created" : fmt_datetime(row["DateCreated"]),
                "date_updated" : fmt_datetime(row["DateUpdated"]),
                "associate_id" : row["UserID"]
            }

            bulk_create.append(Client(**csv2db_client))
