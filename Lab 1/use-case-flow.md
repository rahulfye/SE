# Use-Case Flow Specification

## Use Case: Ingest Audit Logs

**Use Case ID:** UC-001  
**Use Case Name:** Ingest Audit Logs  
**Primary Actor:** Enterprise Application  

### Goal

Allow an enterprise application to securely submit structured JSON audit logs to the Centralized Audit Trail Compliance Engine for processing, PII protection, integrity verification, and immutable storage.

### Preconditions

1. The Centralized Audit Trail Compliance Engine is available.
2. The Enterprise Application is authorized to submit audit logs.
3. The audit log is provided in the supported structured JSON format.
4. The audit processing service is operational.

### Postconditions

**Success:**
1. The audit log has been successfully parsed.
2. Sensitive PII has been identified and masked.
3. A SHA-256 integrity hash has been generated.
4. The processed audit record has been stored in the centralized audit repository.
5. The audit record is available for authorized querying and future compliance review.

**Failure:**
1. The invalid or unprocessable audit log is not stored as a valid audit record.
2. An appropriate error is returned to the Enterprise Application.
3. The failure is recorded for operational monitoring where applicable.

## Main Success Scenario

1. The Enterprise Application submits a structured JSON audit log to the system.
2. The system receives the audit log and validates its basic structure.
3. The system parses the JSON audit log.
4. The system identifies sensitive PII fields within the audit record.
5. The system masks the identified PII according to the configured privacy rules.
6. The system generates a SHA-256 integrity hash for the processed audit record.
7. The system stores the masked audit record and its integrity hash in the centralized immutable audit repository.
8. The system confirms successful processing to the Enterprise Application.

## Alternative Flow

### A1 — Invalid JSON Audit Log

1. The Enterprise Application submits an audit log containing invalid or malformed JSON.
2. The system attempts to parse the submitted audit log.
3. The parsing operation fails.
4. The system rejects the audit record.
5. The system returns an error indicating that the submitted audit log is invalid.
6. The invalid record is not stored in the centralized audit repository.

## Included Use Cases

The **Ingest Audit Logs** use case includes:

- Parse JSON Audit Logs
- Detect PII
- Mask PII
- Generate SHA-256 Hash
- Store Audit Record

These included functions are required to successfully process and securely store an audit record.