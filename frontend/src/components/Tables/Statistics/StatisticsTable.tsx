import { BarChart } from '@mui/x-charts/BarChart';
import { PieChart } from '@mui/x-charts/PieChart';
import { useDrawingArea } from '@mui/x-charts/hooks';
import { styled } from '@mui/material/styles';

import "../Tables.css";
import { StatisticsTitleRow } from "./StatisticsTitleRow";
import { StatisticsRow } from "./StatisticsRow";
import { TablePagination } from '../TablePagination';
import { DataLoadError } from "../../DataLoadError/DataLoadError";
import { useStatisticsTable } from "../../../hooks/useTables/useStatisticsTable";


const size = {
  width: 400,
  height: 300,
};

const StyledText = styled('text')(({ theme }) => ({
  fill: theme.palette.text.primary,
  textAnchor: 'middle',
  dominantBaseline: 'central',
  fontSize: 20,
}));

function PieCenterLabel({ children }: { children: React.ReactNode }) {
  const { width, height, left, top } = useDrawingArea();
  return (
    <StyledText x={left + width / 2} y={top + height / 2}>
      {children}
    </StyledText>
  );
}


export function StatisticsTable() {
	const { 
		statistics,
		statusCodeChart,
		methodChart,
		amountStatistics,
		page, 
		rowsPerPage,
		error,
		handleUpdateTable,
		handleChangePage, 
		handleChangeRowsPerPage,
	} = useStatisticsTable();

	const statusCodeData = [
		{ value: statusCodeChart?.x200 as number, label: '200' },
		{ value: statusCodeChart?.x300 as number, label: '300' },
		{ value: statusCodeChart?.x400 as number, label: '400' },
		{ value: statusCodeChart?.x500 as number, label: '500' },
	];

	const methodData = [
		{ value: methodChart?.OPTIONS as number, label: 'OPTIONS' },
		{ value: methodChart?.GET as number, label: 'GET' },
		{ value: methodChart?.CONNECT as number, label: 'CONNECT' },
		{ value: methodChart?.POST as number, label: 'POST' },
		{ value: methodChart?.PUT as number, label: 'PUT' },
		{ value: methodChart?.DELETE as number, label: 'DELETE' },
		{ value: methodChart?.HEAD as number, label: 'HEAD' },
		{ value: methodChart?.TRACE as number, label: 'TRACE' },
		{ value: methodChart?.PATCH as number, label: 'PATCH' },
	];
	return (
		<>
			<div className="flex flex-row h-full">
				<div className="flex flex-col h-full mr-5">
					<PieChart 
						series={[{data: statusCodeData, innerRadius: 80 }]
					} {...size}>
						<PieCenterLabel>Status</PieCenterLabel>
					</PieChart>

					<PieChart 
						series={[{data: methodData, innerRadius: 80 }]
					} {...size}>
						<PieCenterLabel>Method</PieCenterLabel>
					</PieChart>
				</div>

				<div className="mx-5 table">
					<StatisticsTitleRow />

					<div className="rows-container">
						{ !error
							?	<div className="rows">
									{ statistics.map((item, index) => 
											<StatisticsRow 
												key={ item.id }
												statistics={ item } 
												addClassName={index % 2 ? "bg-gray-200": "bg-white"}
											/>
										)
									}
								</div>
							: <DataLoadError 
									handleUpdate={ handleUpdateTable }
								/>
						}
					</div>

					<TablePagination
						amountItems={ amountStatistics }
						page={ page }
						handleChangePage={ handleChangePage }
						rowsPerPage={ rowsPerPage }
						handleChangeRowsPerPage={ handleChangeRowsPerPage }
					/>
				</div>
			</div>
		</>
	)
}
