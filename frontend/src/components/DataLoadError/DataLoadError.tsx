import "./DataLoadError.css";
import { ErrorIcon } from "../Icons/ErrorIcon";
import { UpdateIcon } from "../Icons/UpdateIcon";


interface DataLoadErrorProps {
	handleUpdate?: () => Promise<void>
}

export function DataLoadError({ handleUpdate }: DataLoadErrorProps) {
	return (
		<div className={ "container-load-error" }>
			<ErrorIcon color="#4b5563" />
			<p className="text-load-error">
				Ошибка загрузки данных
			</p>

			<div 
				className="container-update"
				onClick={ handleUpdate }
			>
				<UpdateIcon color="#197aca" />
				<p className="text-update">
					ОБНОВИТЬ
				</p>
			</div>
		</div>
	)
}
