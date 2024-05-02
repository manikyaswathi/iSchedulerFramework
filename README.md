# iSchedulerFramework
The ICICLE Smart Scheduler Framework - components and independent deployment Instructions. 


In modern high-performance computing (HPC) centers like the Ohio Supercomputer Center (OSC), Texas Advanced Computing Center (TACC), and San Diego Supercomputer Center (SDSC), a significant portion of scientific workloads are driven by artificial intelligence (AI), particularly Deep Neural Network (DNN) training tasks. Efficiently managing and scheduling these AI-driven workloads using SLURM interfaces requires a comprehensive understanding of available resources, allocation policies, and suitable execution configurations tailored to the specific requirements and limitations of the utilized models.
Traditional job scheduling methods, which often involve using default configurations, making adjustments as necessary, or requesting maximum available limits, have their limitations. These approaches can lead to job interruptions due to underprovisioning, prolonged wait times, inefficient resource utilization, and increased costs from overprovisioning. These issues can ultimately result in degraded cluster performance, highlighting the need for a more efficient and optimized approach. Figure 1 shows the conventional HPC user interaction for job submission, monitoring, and execution. 

![Convetional User-HPC Interactions](https://github.com/manikyaswathi/iSchedulerFramework/blob/main/ConvLifeCycle.png?raw=true)


