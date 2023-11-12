##Issue Summary

We had just released a new feature to our recently launched Ruby on Rails site that we had our first intake of users complaining about the site.
5 minutes after we performed a feature update, we started receiving emails from our users talking about "they can't sign in or sign up to our platform".
It was surprising to us because we knew it worked on our machines. About 127 of such emails came to our inbox.
Knowing how hard it can be to attract and keep users, we couldn't afford to lose our users in that way and decided to take a closer look at the problem.
We cloned our site's repository from GitBug, followed the installation instructions and to our surprise the site couldn't startup.
It wasn't long before we realized that the cause of the problem was failing to update the requirements for our project.
The site was malfunctioning from 9:55 AM GMT+1 to 11:20 AM GMT+1.

##Timeline

05-02-2022 9:55 AM GMT+1 - A customer complained that they couldn't sign to the site.
05-02-2022 10:20 AM GMT+1 - One of our backend developers experienced the same issues.
05-02-2022 10:35 AM GMT+1 - We investigated the controllers and the views.
05-02-2022 10:40 AM GMT+1 - We assumed one of our site's dependencies gem being used was at fault or used incorrectly.
05-02-2022 11:00 AM GMT+1 - The incident was escalated to the backend development team.
05-02-2022 11:20 AM GMT+1 - The incident was resolved by updating the requirements for the backend server.

##Root Cause And Resolution

The version of the bcrypt gem we used was outdated. It was raising an error over a hash that was clearly valid.
The hash we were creating was not supported by the version of bcrypt we had installed.
W fixed the issue by manually updating the version of bcrypt in the Gemfile.lock file to a recent version and reinstalling the required gems, and it worked.

##Corrective And Preventative Measures

Setup an integration pipeline to run a build on each pull request branch.
Setup a monitoring system for the database and application servers to keep track of any issue.
Develop tests that need to be passed for each new feature and those tests should be passing before they are merged.
