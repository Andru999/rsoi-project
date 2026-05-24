import "../Tables.css";
import { ArrowIcon } from "../../Icons/ArrowIcon";
import { SortFlights } from "../../../enums/SortFlights";
import { useFlightsSort } from "../../../hooks/useTables/useFlightsSort";


interface FlightsTableColumnProps {
	nameColumn: string
	sortAsc: SortFlights
	sortDesc: SortFlights
	sortTable: SortFlights
	handleChangeSort: (sort: SortFlights) => void
	addClassName?: string
}

export function FlightsTableColumn(props: FlightsTableColumnProps) {
	const { 
		sort, 
		visibility,
		handleClicked, 
		handleMouseEnter, 
		handleMouseLeave,
	} = useFlightsSort({ 
		sortAsc: props.sortAsc,
		sortDesc: props.sortDesc, 
		sortTable: props.sortTable,
		handleChangeSort: props.handleChangeSort,
	});

	const color = sort === props.sortAsc || sort === props.sortDesc ? "white" : "#acc1d4";
	
	return (
		<div 
			className={`title-row-item ${props.addClassName}`}
			onClick={ handleClicked }
			onMouseEnter={ handleMouseEnter}
			onMouseLeave={ handleMouseLeave }
		>
			{ props.nameColumn }
			{ visibility && 
				<ArrowIcon
					upward={ sort !== props.sortDesc }
					color={ color }
					addClassName="py-2 px-2"
					addContainerClassName="basis-16"
				/>
			}
		</div>
	)
}
