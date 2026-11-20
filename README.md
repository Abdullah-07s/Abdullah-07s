<div align="left">

# Hi, I'm Abdullah 👋

<img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=600&size=23&duration=3000&pause=1200&color=C8A03D&center=true&vCenter=true&width=700&lines=Designing+Reliable+Systems;Building+Scalable+Applications;Engineering+Intelligent+Solutions;Creating+Production-Ready+Software"/>

<p align="center">
    <img src="assets/repository-thought.svg" width="850" alt="Repository Thought">
</p>

<br>

[![Portfolio](https://img.shields.io/badge/Portfolio-222222?style=for-the-badge&logo=githubpages&logoColor=white)](https://abdullah-07s.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdullah-mallick-14322b371/)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdullah.mallickk@gmail.com)

</div>

---

# About

I'm a backend developer who likes building systems that talk to each other: APIs, event streams, and the occasional AI feature that has to cite its sources. Final-year CS student at FAST-NUCES Islamabad, based in Pakistan (UTC+5), and 
I did a Java internship at Aksa SDS, where I built and presented Spring Boot projects under senior-engineer review. Everything below is code you can open and run.

---

## Projects I'm proudest of
 
### 🏦 [Helix](https://github.com/Abdullah-07s/Helix-Banking): a digital banking backend
A banking system split into four Spring Boot services (accounts, transactions, cards, fraud) behind a Spring Cloud Gateway, each with its own MySQL schema. Transfers are concurrency-safe, transaction events flow through Kafka, and the fraud service raises alerts over RabbitMQ. JWTs are forwarded between services so ownership checks still apply downstream. Built as a learning project to see how this kind of system actually fits together, with a Jenkins pipeline and Docker Compose for the infrastructure.
`Java 21` `Spring Boot` `Kafka` `RabbitMQ` `MySQL` `Jenkins`
 
### 🤖 [Cognify](https://github.com/Abdullah-07s/Cognify): chat with your documents
Upload PDFs, DOCX, or TXT files and ask questions. Answers stream in live, show the source chunks they came from, and the assistant says "I don't know" when your documents don't contain the answer instead of guessing. Embeddings run locally (sentence-transformers), so only the final generation step calls an API. The demo login is mocked, and I say so in the README.
`FastAPI` `LangChain` `ChromaDB` `Groq (Llama)` `React` `Docker`
 
### 💰 [Nexo](https://github.com/Abdullah-07s/Nexo-Expense-Tracker): expense tracker, deployed
A full-stack expense tracker with JWT auth, monthly category budgets, over-budget alerts, charts, and Swagger docs. Backend and database run on Railway, frontend on Vercel.
<!-- TODO: add your live Nexo URL here, e.g. **[Try it live →](https://your-nexo-url)** -->
`Spring Boot` `PostgreSQL` `React` `Tailwind`
 
### 📊 [Crime Analytics](https://github.com/Abdullah-07s/Crime-Analytics): Lambda architecture on 7M+ rows
A batch-plus-streaming pipeline over the Chicago crime dataset (about 5.7 GB). PySpark handles trend analysis and K-Means hotspot detection, while Kafka and Storm run sliding-window anomaly alerts. The "live" stream is a replay of the CSV at a configurable rate, not a real feed. Results land in Postgres and MongoDB and are served through a Streamlit dashboard.
`PySpark` `Kafka` `Storm` `PostgreSQL` `MongoDB` `Docker`
 
More in my [repositories](https://github.com/Abdullah-07s?tab=repositories): a reactive crypto tracker with WebFlux and R2DBC, a Kafka/Spring Cloud Stream service, a ticket-booking simulator that fixes race conditions three different ways, and all 23 GoF design patterns implemented in Spring Boot.
 
---
 
## What I'm working on now
 
- Finishing my final-year project, **Sentinel Z**: a zero-knowledge-proof-gated Ethereum smart wallet (Solidity, Circom, Groth16). It's private for now.
- Studying MLOps this semester, so more of my projects can ship with tracking, deployment, and monitoring instead of just a notebook.

# Technologies

## Languages

<p align="left">
<img src="https://skillicons.dev/icons?i=java,python,cpp,c,js,solidity" />
</p>

<p align="left">
<img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/x86_Assembly-525252?style=for-the-badge"/>
</p>

---

## Backend & Frameworks

<p align="left">
<img src="https://skillicons.dev/icons?i=spring,react,docker,maven,git,github" />
</p>

<p align="left">
<img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot"/>
<img src="https://img.shields.io/badge/Spring_Security-6DB33F?style=for-the-badge&logo=springsecurity"/>
<img src="https://img.shields.io/badge/Spring_Data_JPA-6DB33F?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Spring_Cloud_Stream-6DB33F?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Spring_Cloud_Gateway-6DB33F?style=for-the-badge"/>
<img src="https://img.shields.io/badge/WebSocket-010101?style=for-the-badge"/>
<img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens"/>
<img src="https://img.shields.io/badge/REST_API-005571?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
</p>

---

## Databases

<p align="left">
<img src="https://skillicons.dev/icons?i=mysql,postgres,mongodb,sqlite" />
</p>

<p align="left">
<img src="https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoftsqlserver"/>
<img src="https://img.shields.io/badge/R2DBC-6DB33F?style=for-the-badge"/>
</p>

---

## AI & Machine Learning

<p align="left">
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas"/>
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn"/>
<img src="https://img.shields.io/badge/PyMC-3776AB?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/RAG_Pipelines-444444?style=for-the-badge"/>
<img src="https://img.shields.io/badge/ChromaDB-444444?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge"/>
</p>

---

## Big Data & Distributed Systems

<p align="left">
<img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark"/>
<img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apachekafka"/>
<img src="https://img.shields.io/badge/Apache_Storm-225593?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Apache_Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black"/>
<img src="https://img.shields.io/badge/Lambda_Architecture-444444?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Event--Driven_Architecture-444444?style=for-the-badge"/>
</p>

---

## Messaging & Integration

<p align="left">
<img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apachekafka"/>
<img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenFeign-6DB33F?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Server--Sent_Events-444444?style=for-the-badge"/>
</p>

---

## Blockchain

<p align="left">
<img src="https://skillicons.dev/icons?i=solidity" />
</p>

<p align="left">
<img src="https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=ethereum"/>
<img src="https://img.shields.io/badge/Hardhat-FFF100?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Circom-2D2D2D?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Groth16-444444?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Zero--Knowledge_Proofs-6F42C1?style=for-the-badge"/>
</p>

---

## Software Engineering

<p align="left">
<img src="https://img.shields.io/badge/OOP-00599C?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SOLID-1E88E5?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Design_Patterns-6DB33F?style=for-the-badge"/>
<img src="https://img.shields.io/badge/System_Design-222222?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Microservices-444444?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Agile-FF6F00?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Scrum-009FDA?style=for-the-badge"/>
</p>

---

## Developer Tools & Infrastructure

<p align="left">
<img src="https://skillicons.dev/icons?i=idea,vscode,postman,linux,docker,git,github,jenkins" />
</p>

---

# GitHub

<div align="center">

[![GitHub Streak](https://streak-stats.demolab.com?user=Abdullah-07s&theme=github-dark-blue&hide_border=true)](https://git.io/streak-stats)

</div>

---

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=500&size=22&duration=3500&pause=1200&color=C8A03D&center=true&vCenter=true&width=650&lines=Write+code+that+works.;Engineer+systems+that+last."/>

</div>
