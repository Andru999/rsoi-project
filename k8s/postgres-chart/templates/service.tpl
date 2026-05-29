{{- define "service.template" }}
apiVersion: v1
kind: Service
metadata:
  name: {{ .service.name }}
  labels:
    app.kubernetes.io/name: {{ .service.name }}
    app.kubernetes.io/version: "{{ .ctx.Values.version }}"
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: simple-backend
    app.kubernetes.io/managed-by: helm
spec:
  selector:
    app: {{ .service.name }}
  ports:
    - name: postgresql
      port: {{ .ctx.Values.port }}
      targetPort: {{ .ctx.Values.port }}
{{- end }}