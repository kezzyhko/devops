# Best practices about CI

This file contains some best practices I found about the CI:
* In general, the workflow should not require manual input
* Workflows should not include passwords and tokens, there are specific mechanism for keeping passwords in all CI tools (GitHub secrets, Jenkins credentials)
* Code should be tested before publishing
* CI should be the only way to publish app to the production
* Prefer declarative syntax over scripted syntax
* Do not make all the work in single stage. Stages should be logically separated.
