# -----------------------
# Terraform configuration
# -----------------------
terraform {
  required_version = ">=0.13"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# -----------------------
# Variables
# -----------------------

provider "aws" {
  region = var.region
}

variable "region" {
  default = "ap-northeast-1"
}

variable "aws_account_id" {
  type = string
}

variable "project" {
  type = string
}

variable "environment" {
  type = string
}