import "../Tables.css";
import { IFilterFlight } from "../../../interfaces/Flight/IFilterFlight";
import { FilterIcon } from "../../Icons/FilterIcon";
import { useFilterFlightsIcon } from "../../../hooks/useIcons/useFilterFlightsIcon";


interface FlightsTableFilterProps {
	filterTable: IFilterFlight
	handleOpenWindow: () => void
}

export function FlightsTableFilter({ filterTable, handleOpenWindow }: FlightsTableFilterProps) {
	const { 
		active,
	} = useFilterFlightsIcon({ filterTable });

	return (
		<FilterIcon
			color="white"
			selected={ active }
			onClick={ handleOpenWindow }
			addClassName="py-2 px-2 hover:bg-white/10"
			addContainerClassName="basis-1/2"
		/>
	)
}
