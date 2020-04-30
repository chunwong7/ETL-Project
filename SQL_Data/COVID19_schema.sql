-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/J1haF1
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- ERD diagram for etl project
CREATE TABLE "dates" (
    "state" VARCHAR   NOT NULL,
    "mass_gathering_restriction" date ,
    "initial_business_closure" date ,
    "educational_facilities_closure" date ,
    "nonessential_services_closure" date ,
    "stay_at_home_order" date ,
    "travel_severely_limited" date ,
    CONSTRAINT "pk_dates" PRIMARY KEY (
        "state"
     )
);

CREATE TABLE "forecast" (
    "key" int   NOT NULL,
    "model" VARCHAR   NOT NULL,
    "forecast_date" date   NOT NULL,
    "target" VARCHAR   NOT NULL,
    "target_end_date" date   NOT NULL,
    "state" VARCHAR   NOT NULL,
    "actual" int   NOT NULL,
    "quantile_0.025" float   NOT NULL,
    "quantile_0.975" float   NOT NULL,
    CONSTRAINT "pk_forecast" PRIMARY KEY (
        "key"
     )
);

CREATE TABLE "counties" (
    "Index" int   NOT NULL,
    "FIPS" float   NOT NULL,
    "County" VARCHAR   NOT NULL,
    "State" VARCHAR   NOT NULL,
    "Lat" float   NOT NULL,
    "Lng" float   NOT NULL,
    "Combined_Key" VARCHAR   NOT NULL,
    "Date" date   NOT NULL,
    "Confirmed" int   NOT NULL,
    "Deaths" int   NOT NULL,
    CONSTRAINT "pk_counties" PRIMARY KEY (
        "Index"
     )
);

CREATE TABLE "states" (
    "State" VARCHAR   NOT NULL,
    "Date" date   NOT NULL,
    "Total_cases" int   NOT NULL,
    "New_cases" int ,
    "Total_deaths" int   NOT NULL,
    "New_deaths" int ,
    "Active_cases" int   NOT NULL,
    "Cases_per_million" int   NOT NULL,
    "Deaths_per_million" int   NOT NULL,
    "Total_tests" int   NOT NULL,
    "Tests_per_million" int   NOT NULL,
    CONSTRAINT "pk_states" PRIMARY KEY (
        "State"
     )
);

CREATE TABLE "hospitals" (
    "state" VARCHAR   NOT NULL,
    "hospital_beds_needed" int   ,
    "hospital_beds_available" int   ,
    "hospital_beds_shortage" int   ,
    "icu_beds_needed" int   ,
    "icu_beds_available" int   ,
    "icu_beds_shortage" int   ,
    "ventilators_needed" int   ,
    CONSTRAINT "pk_hospitals" PRIMARY KEY (
        "state"
     )
);

ALTER TABLE "dates" ADD CONSTRAINT "fk_dates_state" FOREIGN KEY("state")
REFERENCES "states" ("State");

ALTER TABLE "forecast" ADD CONSTRAINT "fk_forecast_state" FOREIGN KEY("state")
REFERENCES "states" ("State");

ALTER TABLE "counties" ADD CONSTRAINT "fk_counties_State" FOREIGN KEY("State")
REFERENCES "states" ("State");

ALTER TABLE "hospitals" ADD CONSTRAINT "fk_hospitals_state" FOREIGN KEY("state")
REFERENCES "states" ("State");
