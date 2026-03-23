# ETL PIPELINE

The goal of this module is to create a reusable, easy-to-test, and ready to deploy pipeline.

The configuration layer will be abstracted so that any future ETL process can reference it, simplifying its creation.
The execution steps will be well-defined, allowing for the seamless creation and reading of new ETL processes.

Each ETL process will operate independently and is designed to be easy to test.

Another key focus is data security and structure. To achieve this, tables will be abstracted into separate files that define their structure and data types.

The short-term goal, as of today (March 23, 2026), is to be able to execute Python with the `<etl>` argument, which represents the ETL job to be run.