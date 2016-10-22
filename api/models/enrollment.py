from django.db import models

class EnrollmentManager(models.Manager):
    pass

class Enrollment(models.Model):
    objects = EnrollmentManager()
    personal_id = models.CharField(max_length=15)
    project_entry_id = models.CharField(max_length=15)
    entry_date = models.DateField(null=False)
    household_id = models.CharField(max_length=15)
    relationship_to_head_of_household = models.IntegerField(null=True)
    residence_prior = models.IntegerField(null=True)
    other_residence_prior = models.IntegerField(null=True)
    residence_prior_length_of_stay = models.IntegerField(null=True)
    disabling_condition = models.IntegerField(null=True)
    entry_from_street_essh = models.IntegerField(null=True)
    date_to_street_essh = models.DateField(null=True)
    times_homeless_past_three_years = models.IntegerField(null=True)
    month_homeless_past_three_years = models.IntegerField(null=True)
    housing_status = models.IntegerField(null=True)
    date_of_engagement = models.DateField(null=True)
    in_permanent_housing = models.NullBooleanField()
    residential_move_in_date = models.DateField(null=True)
    date_of_path_status = models.DateField(null=True)
    client_enrolled_in_path = models.NullBooleanField()
    reason_not_enrolled = models.IntegerField(null=True)
    worst_housing_situation = models.IntegerField(null=True)
    percent_ami = models.IntegerField(null=True)
    last_permanent_street = models.CharField(max_length=127)
    last_permanent_city = models.CharField(max_length=31)
    last_permanent_state = models.CharField(max_length=7)
    last_permanent_zip = models.CharField(max_length=7)
    date_of_bcp_status = models.DateField(null=True)
    fysb_youth = models.NullBooleanField()
    reason_no_services = models.IntegerField(null=True)
    sexual_orientation = models.IntegerField(null=True)
    formar_ward_child_welfare = models.IntegerField(null=True)
    juvenile_justice_years = models.IntegerField(null=True)
    juvenile_justice_months = models.IntegerField(null=True)
    houshold_dynamics = models.NullBooleanField()
    sexual_orientation_gender_identity_youth = models.NullBooleanField()
    sexual_orientation_gender_identity_family = models.NullBooleanField()
    housing_issues_youth = models.NullBooleanField()
    housing_issues_family = models.NullBooleanField()
    school_or_educational_issues_youth = models.NullBooleanField()
    school_or_educational_issues_family = models.NullBooleanField()
    unemployment_family = models.NullBooleanField()
    mental_health_issues_youth = models.NullBooleanField()
    mental_health_issues_family = models.NullBooleanField()
    health_issues_youth = models.NullBooleanField()
    health_issues_familty = models.NullBooleanField()
    physical_disability_youth = models.NullBooleanField()
    physical_disability_fam = models.NullBooleanField()
    mental_disability_youth = models.NullBooleanField()
    mental_disability_fam = models.NullBooleanField()
    abuse_and_neglect_youth = models.NullBooleanField()
    abuse_and_neglect_fam = models.NullBooleanField()
    alcohol_drug_abuse_youth = models.NullBooleanField()
    alcohol_drug_abuse_fam = models.NullBooleanField()
    insufficient_income = models.NullBooleanField()
    active_military_parent = models.NullBooleanField()
    incarcerated_parent = models.NullBooleanField()
    incarcerated_parent_status = models.IntegerField(null=True)
    referral_source = models.IntegerField(null=True)
    exchange_for_sex = models.IntegerField(null=True)
    exchange_for_sex_past_three_months = models.IntegerField(null=True)
    count_of_exchange_for_sex = models.IntegerField(null=True)
    asked_or_forced_to_exchange_for_sex = models.IntegerField(null=True)
    work_place_violence_threats = models.IntegerField(null=True)
    work_place_promise_difference = models.IntegerField(null=True)
    coerced_to_continue_work = models.IntegerField(null=True)
    labor_exploit_past_three_months = models.IntegerField(null=True)
    hp_screening_score = models.IntegerField(null=True)
    vamc_station = models.IntegerField(null=True)
    date_created = models.DateTimeField(null=False)
    date_updated = models.DateTimeField(null=False)
    associate_id = models.CharField(max_length=15)