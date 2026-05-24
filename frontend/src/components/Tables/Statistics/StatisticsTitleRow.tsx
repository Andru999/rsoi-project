import "../Tables.css";


export function StatisticsTitleRow() {
	return (
		<div 
			className="title-row-without-buttons"
		>
			<div className="title-row-item basis-1/6">{ "Метод" }</div>
			<div className="title-row-item basis-1/2">{ "Url" }</div>
			<div className="title-row-item basis-1/6">{ "Статус" }</div>
			<div className="title-row-item basis-1/4">{ "Время" }</div>
		</div>
	)
}
