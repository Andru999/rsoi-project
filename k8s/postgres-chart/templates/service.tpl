{{- define "service.template" }}
apiVersion: v1
kind: Service
metadata:
  name: {{ .service.name }}
spec:
  {{- if .service.headless }}
  clusterIP: None
  {{- end }}
  type: {{ .service.type | default "ClusterIP" }}
  selector:
    app: {{ .ctx.Release.Name }}-{{ .service.name }}
  ports:
    - port: {{ .service.port }}
      targetPort: {{ .service.targetPort }}
      protocol: TCP
      {{- if and (ne .service.name "kafka-broker") (ne .service.name "zookeeper") }}
      name: http
      {{- end }}
{{- end }}