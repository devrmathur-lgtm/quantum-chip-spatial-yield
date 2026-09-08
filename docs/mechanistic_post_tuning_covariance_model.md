# Mechanistic post-tuning covariance model

A physically interpretable post-tuning model separates retained spatial structure, retained local fabrication variation, and newly introduced prediction/tuning residuals:

\[
\Sigma_{\mathrm{post}}
=
\lambda^2 \Sigma_{\mathrm{spatial}}
+
\mu^2 \Sigma_{\mathrm{local}}
+
\tau^2 I.
\]

Interpretation:

- \(\lambda\): fraction of the original smooth spatial component retained after tuning
- \(\mu\): retained local fabrication component
- \(\tau\): newly dominant independent prediction/tuning residual

No physical values should be assigned to these coefficients without data.

This model is intended to prevent the low-spread q sweep from being interpreted as if q simply and arbitrarily changes. Different manufacturing and tuning routes can alter the covariance components differently.
