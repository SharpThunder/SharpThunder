<h1 align="center">Hi, I'm Sinan ⚡</h1>
<p align="center"><b>DevOps Engineer · Warsaw, Poland</b><br>
I build and run cloud infrastructure: Terraform, Kubernetes and CI/CD across AWS, Azure and GCP.</p>

<p align="center">
  <a href="https://sharpthunder.github.io"><img src="https://img.shields.io/badge/site-sharpthunder.github.io-0b7285?style=flat-square&logo=githubpages&logoColor=white" alt="Website"></a>
  <a href="https://www.linkedin.com/in/sinan-b-%C3%B6zt%C3%BCrk-589b1279/"><img src="https://img.shields.io/badge/LinkedIn-connect-0a66c2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://sharpthunder.github.io/blog/"><img src="https://img.shields.io/badge/blog-read-555?style=flat-square&logo=rss&logoColor=white" alt="Blog"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CKA-Certified_Kubernetes_Administrator-326ce5?style=flat-square&logo=kubernetes&logoColor=white" alt="CKA">
  <img src="https://img.shields.io/badge/AWS-Solutions_Architect_Associate-ff9900?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS SAA">
  <img src="https://img.shields.io/badge/HashiCorp-Terraform_Associate-7b42bc?style=flat-square&logo=terraform&logoColor=white" alt="Terraform Associate">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=aws,azure,gcp,kubernetes,terraform,docker,githubactions,linux,bash,python,nginx,prometheus,grafana&perline=13" alt="Stack">
</p>

---

### 🛠️ What I work on

```yaml
now:
  role: DevOps Engineer, Ulula (EcoVadis)
  clouds: [AWS EU, AWS China, GCP]
  iac: Terraform, 25+ reusable modules across both AWS partitions
  ci_cd: Azure DevOps, Git Flow, zero-downtime releases, OIDC (no static keys)
  kubernetes: Helm chart PoC for moving from EC2 to Kubernetes
before:
  - PowerDev: EKS/Rancher with Terraform + eksctl, AWS -> Azure migration (10 TB Aurora PostgreSQL),
              solver scaled to 300 cores on AKS + Knative
  - Gözen Holding: on-prem VMware -> OpenNebula, Rancher/RKE, HAProxy, Zabbix across 300+ servers
building: homelab (k3s, Terraform, ArgoCD, Prometheus), in progress
```

### 📐 Projects

| Project | What it is |
|---|---|
| [**eks-platform-design**](https://github.com/SharpThunder/eks-platform-design) | EKS platform for a RealWorld app at millions of users: 3-AZ network, GitHub Actions on autoscaling runners, Prometheus + Loki, and what I'd change in 2026 |
| [**sharpthunder.github.io**](https://github.com/SharpThunder/sharpthunder.github.io) | My site and blog (Jekyll on GitHub Pages) |

### ☸️ Kubernetes open source

**Merged pull requests**

| Project | PR | What it fixed |
|---|---|---|
| <img src="https://skillicons.dev/icons?i=kubernetes" width="16"> **rancher/fleet** | [#1185](https://github.com/rancher/fleet/pull/1185) ![merged](https://img.shields.io/badge/-merged-8250df?style=flat-square) | Disabling the GitOps feature broke the Fleet controller deployment |
| <img src="https://skillicons.dev/icons?i=aws" width="16"> **eksctl-io/eksctl** | [#4047](https://github.com/eksctl-io/eksctl/pull/4047) ![merged](https://img.shields.io/badge/-merged-8250df?style=flat-square) | Missing IAM permission on the EKS minimum-permissions page |

**Bugs found running Kubernetes in production**

| Project | Issue | What I hit |
|---|---|---|
| rancher/rancher | [#36465](https://github.com/rancher/rancher/issues/36465) | Rancher deleted EKS nodegroups when importing an EKS cluster |
| rancher/rancher | [#37940](https://github.com/rancher/rancher/issues/37940) | Rancher broke after an EKS version upgrade done from the AWS console |
| rancher/rancher | [#34690](https://github.com/rancher/rancher/issues/34690) | Feature request: zone awareness for EKS nodegroups |
| elastic/cloud-on-k8s | [#4835](https://github.com/elastic/cloud-on-k8s/issues/4835) | APM server errors in Kibana on a fresh ECK stack |
| kodekloudhub/cka-course | [#178](https://github.com/kodekloudhub/certified-kubernetes-administrator-course/issues/178) | Apple Silicon lab script failed on paths with spaces |

### 🔭 On my radar

I've starred **1,100+ repositories since 2016**. It's how I keep up with the ecosystem. A few I keep coming back to:

| Kubernetes | IaC & delivery | Observability | Security |
|---|---|---|---|
| [k3s](https://github.com/k3s-io/k3s) | [terragrunt](https://github.com/gruntwork-io/terragrunt) | [SigNoz](https://github.com/SigNoz/signoz) | [trivy](https://github.com/aquasecurity/trivy) |
| [k9s](https://github.com/derailed/k9s) | [OpenTofu](https://github.com/opentofu/manifesto) | [k6](https://github.com/grafana/k6) | [prowler](https://github.com/prowler-cloud/prowler) |
| [cilium](https://github.com/cilium/cilium) | [infracost](https://github.com/infracost/infracost) | [OpenObserve](https://github.com/openobserve/openobserve) | [semgrep](https://github.com/semgrep/semgrep) |
| [talos](https://github.com/siderolabs/talos) | [argo-cd](https://github.com/argoproj/argo-cd) | [uptime-kuma](https://github.com/louislam/uptime-kuma) | [wazuh](https://github.com/wazuh/wazuh) |
| [vcluster](https://github.com/loft-sh/vcluster) | [renovate](https://github.com/renovatebot/renovate) | [osquery](https://github.com/osquery/osquery) | [sealed-secrets](https://github.com/bitnami/sealed-secrets) |
| [Reloader](https://github.com/stakater/Reloader) | [act](https://github.com/nektos/act) | [below](https://github.com/facebookincubator/below) | [How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server) |

#### 📊 What my stars say

<!-- STATS:START -->
```text
1,166 repos starred since 2016

Kubernetes             ████████████████████████ 301
Security               ███████████████          183
Containers             ██████████               129
Cloud (AWS/Azure/GCP)  █████████                110
Observability          ██████                   81
IaC                    █████                    61
CI/CD & GitOps         █████                    61
Self-hosted & homelab  ██                       25
```
<!-- STATS:END -->

#### ⭐ Recently starred

<!-- STARRED:START -->
| Repo | What it is | ⭐ |
|---|---|---|
| [openchoreo/openchoreo](https://github.com/openchoreo/openchoreo) | OpenChoreo is an internal developer platform for Kubernetes | 1,598 |
| [floci-io/floci](https://github.com/floci-io/floci) | Light, fluffy, and always free - The AWS Local Emulator alternative | 25,828 |
| [epam/BrainTF](https://github.com/epam/BrainTF) | AI tools for remediation and security analysis of Terraform code | 14 |
| [abhayraghuwanshi/k8s-ingress-gen](https://github.com/abhayraghuwanshi/k8s-ingress-gen) | yaml generator | 117 |
| [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | macOS menu bar app that tells you, in plain English, what each USB-C cable plugged into... | 8,789 |
| [floci-io/floci-az](https://github.com/floci-io/floci-az) | Light, fluffy, and always free - Local Azure Emulator | 691 |
| [antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill) | Terraform & OpenTofu Skill for AI Agents - testing, modules, CI/CD, and production patt... | 2,384 |
| [alexellis/k3sup](https://github.com/alexellis/k3sup) | bootstrap K3s over SSH in < 60s 🚀 | 7,430 |
<!-- STARRED:END -->

<sub>This list updates itself weekly via a <a href=".github/workflows/starred.yml">GitHub Actions workflow</a>.</sub>

---

<p align="center"><sub>Off-call: bicycles, travel, games and a homelab that is never finished.</sub></p>
