import "../Tables.css";
import { IStatistics } from "../../../interfaces/Statistics/IStatistics";


interface StatisticsRowProps {
	statistics: IStatistics
	addClassName?: string
}

export function StatisticsRow(props: StatisticsRowProps) {
	return (
		<div
			className={ `row ${ props.addClassName }` }
		>
			<div className="row-item basis-1/6">{ props.statistics.method }</div>
			<div className="row-item basis-1/2">{ props.statistics.url }</div>
			<div className="row-item basis-1/6">{ props.statistics.status_code }</div>
			<div className="row-item basis-1/4">{ props.statistics.time }</div>
		</div>
	)
}
