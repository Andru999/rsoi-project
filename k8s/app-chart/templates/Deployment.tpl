{{- define "deployment.template" }}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .ctx.Release.Name }}-{{.service.name}}-dep
  labels:
    app: {{ .ctx.Release.Name }}-{{.service.name}}

spec:
  replicas: {{.service.replicaCount}}

  selector:
    matchLabels:
      app: {{ .ctx.Release.Name }}-{{.service.name}}

  template:
    metadata:
      name: {{ .ctx.Release.Name }}-{{.service.name}}
      labels:
        app: {{ .ctx.Release.Name }}-{{.service.name}}

    spec:
      containers:
        - name: {{ .ctx.Release.Name }}-{{.service.name}}
          image: {{.service.container}}
          imagePullPolicy: {{ .service.imagePullPolicy | default "Always" }}

          {{- if and (hasKey .service "port") (gt (int .service.port) 0) }}
          ports:
            - containerPort: {{ .service.targetPort | default .service.port }}
              protocol: TCP
              {{- if ne .service.name "kafka" }}
              name: http
              {{- end }}
          {{- end }}

          env:
            {{- range $k, $v := .service.env}}
            - name: {{$k | quote}}
              value: {{$v | quote}}
            {{- end }}

      restartPolicy: Always
{{- end }}