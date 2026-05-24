import "./Page.css";
import { StatisticsTable } from "../components/Tables/Statistics/StatisticsTable";


interface StatisticsPageProps {
	openMiniDrawer: boolean
}

export function StatisticsPage({ openMiniDrawer }: StatisticsPageProps) {
	return (
		<div className={`${openMiniDrawer ? "short-page-container" : "long-page-container"}`}>
			<StatisticsTable />
		</div>
	)
}
