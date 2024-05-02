# iSchedulerFramework
The ICICLE Smart Scheduler Framework - components and independent deployment Instructions. 


In modern high-performance computing (HPC) centers like the Ohio Supercomputer Center (OSC), Texas Advanced Computing Center (TACC), and San Diego Supercomputer Center (SDSC), a significant portion of scientific workloads are driven by artificial intelligence (AI), particularly Deep Neural Network (DNN) training tasks. Efficiently managing and scheduling these AI-driven workloads using SLURM interfaces requires a comprehensive understanding of available resources, allocation policies, and suitable execution configurations tailored to the specific requirements and limitations of the utilized models.
Traditional job scheduling methods, which often involve using default configurations, making adjustments as necessary, or requesting maximum available limits, have their limitations. These approaches can lead to job interruptions due to underprovisioning, prolonged wait times, inefficient resource utilization, and increased costs from overprovisioning. These issues can ultimately result in degraded cluster performance, highlighting the need for a more efficient and optimized approach. Figure 1 shows the conventional HPC user interaction for job submission, monitoring, and execution. 

![Convetional User-HPC Interactions](https://github.com/manikyaswathi/iSchedulerFramework/blob/main/Images/ConvLifeCycle.png?raw=true)

**Potential Bottlenecks of the current HPC-user interactions**
_**1. CI Awareness:**_
- _Understanding CI Batch Job Limitations (SLURM Configurations) and Consulting Documentation for Constraints:_ Users should understand the limitations associated with CI batch jobs, particularly about SLURM configurations. Users should consult the documentation provided by sources such as OSC and TACC to ascertain memory and walltime caps (both minimum and maximum) for their desired system (node). Additionally, they should identify which queues to request the allocation.
- _Awareness of Maximum User and Account Limitations along with Shared Account Workloads:_  Users should be aware of the maximum number of jobs they can submit and the maximum number of nodes they can allocate across different jobs simultaneously. Users should understand the workloads of fellow users who share the same account, which authorizes specific resource usage and incurs billing.
- _Learning Curve and Optimization:_ Users may initially face a learning curve in understanding these complexities but eventually learn to optimize settings tailored to their workload.
- _Vigilance Regarding Policy Changes and Revisiting Documentation for Policy Updates:_ Users must stay vigilant as CI documentation warns that "the batch limits can change without notice." Regularly checking production documentation pages is essential. Users revisit documentation resources only when their tuned jobs suddenly get affected by changes in CI policies.:


**Solutions Offered via iScheduler Helper:**
1. _Implementation of a Centralized Database:_ We have implemented a dedicated database to store all CI limitations, providing users with a centralized resource for informed decision-making. This database allows users to query whether a specific allocation is viable before initiating the job submission process through SLURM scripts. For detailed guidance on configuring and exploring the database's utility, refer to the readme file in the "DataBase" folder. Additionally, the readme offers insights into additional use cases, expanding on the database's functionality and potential applications.
