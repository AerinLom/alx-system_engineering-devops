# Post-Mortem: E-commerce Website Outage

## Issue Summary

**Duration of the Outage:**
- **Start Time:** May 15, 2024, 12:45 SAST
- **End Time:** May 15, 2024, 15:15 SAST

**Impact:**
- **Service:** E-commerce Website
- **User Experience:** Users were unable to load product pages or experienced extremely slow load times.
- **Affected Users:** Approximately 85% of users attempting to access the website during the outage period.

**Root Cause:**
- A memory leak in the web server application caused the server to run out of memory, leading to service degradation and eventual crashes.

--------------------------------------

## Timeline

- **12:45 SAST:** Issue detected through automated monitoring alerts indicating high memory usage and increased page load times.
- **12:50 SAST:** On-call engineer notified and began initial investigation. Our first clue: the server had as much memory left as a goldfish has attention span.
- **12:55 SAST:** Verified issue through logs showing increasing memory usage and server errors.
- **13:05 SAST:** Initial assumption: Suspected a sudden increase in traffic causing resource exhaustion.
- **13:15 SAST:** Investigated traffic patterns; no significant increase observed.
- **13:30 SAST:** Misleading path: Focused on potential database performance issues, conducted database health checks. The database was healthy .
- **13:45 SAST:** Database team confirmed normal performance with no anomalies.
- **14:00 SAST:** Escalated to the web server team for deeper analysis. Time to call in the big guns.
- **14:15 SAST:** Web server team identified a memory leak in the application code.
- **14:30 SAST:** Temporarily restarted the web servers to mitigate the issue while working on a permanent fix. A quick reboot to shake off the cobwebs.
- **14:45 SAST:** Developers deployed a hotfix to resolve the memory leak. The bug was squashed, and the memory leak plugged.
- **15:00 SAST:** Monitoring showed a decrease in memory usage and improved page load times.
- **15:15 SAST:** Confirmed full resolution of the issue; all services operational. Crisis averted, the server promised to behave.

--------------------------------------

## Root Cause and Resolution

**Root Cause:**
The root cause of the outage was a memory leak in the web server application. A recently deployed update contained a bug that caused the application to retain memory unnecessarily, leading to gradual memory consumption until the server could no longer function properly. In essence, the server turned into a memory blackhole, eating up space.

**Resolution:**
To resolve the issue, the web server team identified the faulty code responsible for the memory leak and developed a hotfix. The hotfix was then deployed to all web servers. Additionally, the servers were restarted to clear the accumulated memory usage, restoring normal operations.

---------------------------------------

## Corrective and Preventative Measures

**Improvements/Fixes:**
1. **Enhanced Code Review:** Implement stricter code review processes to catch potential memory leaks and other issues before deployment. No more sneaky bugs slipping through!
2. **Monitoring Enhancements:** Add detailed monitoring for memory usage patterns and set up alerts for abnormal trends. In case a blackhole spawns in again.
3. **Load Testing:** Conduct comprehensive load testing for new releases to identify performance issues in a controlled environment.
4. **Incident Response Training:** Train the team on efficient incident response to quickly identify and address similar issues in the future.

**Tasks:**
- **Task 1:** Review and enhance the current code review checklist to include checks for memory management practices.
- **Task 2:** Implement additional monitoring for memory usage and set up real-time alerts for the operations team.
- **Task 3:** Schedule regular load testing sessions and incorporate them into the release pipeline.
- **Task 4:** Develop and conduct incident response drills focusing on memory-related issues.
- **Task 5:** Update the deployment process to include a rollback plan for quick reversion in case of detected issues.
