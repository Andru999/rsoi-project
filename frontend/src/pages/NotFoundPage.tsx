import { TextErrorPage } from '../components/Texts/TextErrorPage';


interface NotFoundPageProps {
	openMiniDrawer: boolean
}

export function NotFoundPage({ openMiniDrawer }: NotFoundPageProps) {
	return (
		<TextErrorPage
			header="Страница не найдена"
			text={ "Неправильно набран адрес, или такой \nстраницы больше не существует" }
			openMiniDrawer={ openMiniDrawer }
		/>
	)
}
